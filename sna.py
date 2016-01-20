#!/usr/bin/env python3
import random
from graphviz import Graph
from graphviz import Digraph

class SNAnalyzer(object):
    def __init__(self,inPath,outPath,engine,analyzeType):
            self.network  = {}
            self.nameIndex = {}
            self.inPath = inPath
            self.outPath = outPath
            self.engine = engine
            self.aType = analyzeType
            self.networkFileParse(self.inPath)

    def random_id(self,len):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        id = ''
        for i in range(0,len):
            id += random.choice(alpha)
        return id

    def networkFileParse(self,path):
        f = open(path, 'r')
        for line in f:
            line = line.replace("\n","")
            self.nameIndex.update({line.split(":")[0]:self.random_id(3)})
            self.network.update({line.split(":")[0]:e.split(",") for e in line.split(":")[1:]})
        f.close()


    def graphUpdate(self):
            if self.aType == "tw":
                self.graph = Digraph()
            elif self.aType == "fb":
                self.graph = Graph()
            else:
                exit("Invalid Analyze Type")

            for key in self.nameIndex.keys():
                self.graph.node(self.nameIndex[key], key)
            for key in self.network.keys():
                for friend in self.network[key]:
                    if friend != "":
                        self.graph.edge(self.nameIndex[key],self.nameIndex[friend])

    def generateGraphCode(self):
        self.graphUpdate()
        return self.graph.source

    def renderGraph(self):
        self.graphUpdate()
        self.graph.engine = self.engine
        self.graph.render(self.outPath, view=True)


    def addNode(self,newNode):
            if newNode not in self.nameIndex.keys():
                self.nameIndex[newNode] = self.random_id(3)
                self.network[newNode] = []
            else:
                print("Error: Network already has that {} named Node !".format(newNode))


    def removeNode(self,targetNode):
        if targetNode in self.nameIndex.keys():
            del self.nameIndex[targetNode]
            del self.network[targetNode]
            for key in self.network.keys():
                if targetNode in self.network[key]:
                    self.network[key].remove(targetNode)
        else:
            print("Error: Network not has that {} named Node !".format(targetNode))


    def hasRelation(self,sourceNode,targetNode):
        friends = self.network[sourceNode]
        if targetNode in friends:
            return True
        else:
            return False

    def addRelation(self,sourceNode,targetNode):
        if not self.hasRelation(sourceNode,targetNode):
             self.network[sourceNode].append(targetNode)
        else:
            print("Error: The Node {} is already related to {} !".format(sourceNode, targetNode))


    def removeRelation(self,sourceNode,targetNode):
        if self.hasRelation(sourceNode,targetNode):
             self.network[sourceNode].remove(targetNode)
        else:
            print("Error: The Node {} is not related with {} !".format(sourceNode, targetNode))
