#!/usr/bin/env python3
import sna
SNA = sna.SNAnalyzer(inPath="example_network.txt",outPath="out/example_network.gv",engine="circo",analyzeType="tw")
SNA.addUser("Fenasi Kerim")
SNA.addUser("Nuri Alço")
SNA.addRelation("Fenasi Kerim","Nuri Alço")
SNA.addRelation("Nuri Alço","Fenasi Kerim")
SNA.renderGraph()
