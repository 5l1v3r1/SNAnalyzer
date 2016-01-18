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
            self.networkFileParse(self.inPath)

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
