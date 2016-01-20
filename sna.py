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
        print(self.network)

    def addUser(self,newUser):
        if self.aType == "tw":
            if newUser not in self.nameIndex.keys():
                self.nameIndex[newUser] = self.random_id(3)
                self.network[newUser] = []
                print(self.nameIndex)

    def removeUser(self,targetUser):
        if targetUser in self.nameIndex.keys():
            del self.nameIndex[targetUser]
            del self.network[targetUser]
            for key in self.network.keys():
                if targetUser in self.network[key]:
                    self.network[key].remove(targetUser)


    def hasRelation(self,sourceUser,targetUser):
        friends = self.network[sourceUser]
        if targetUser in friends:
            return True
        else:
            return False

    def addRelation(self,sourceUser,targetUser):
        if not self.hasRelation(sourceUser,targetUser):
             self.network[sourceUser].append(targetUser)


    def removeRelation(self,sourceUser,targetUser):
        if self.hasRelation(sourceUser,targetUser):
             self.network[sourceUser].remove(targetUser)
