#!/usr/bin/env python3
import sna
SNA = sna.SNAnalyzer(inPath="example_network.txt",outPath="out/example_network.gv",engine="circo",analyzeType="tw")
SNA.addNode("Özge Nayır")
SNA.addNode("Faik Özsoy")
SNA.addNode("Melis Alan")
SNA.addNode("Aslı Duman") #Gives Error message
SNA.addNode("Gizem Arslan")
SNA.removeNode("Gizem Arslan")
SNA.removeNode("Kaan As") #Gives Error message
SNA.addRelation(sourceNode="Özge Nayır",targetNode="Ahmet Sezer") #Add Ahmet Sezer to Özge Nayır's friend list.
SNA.addRelation(sourceNode="Ahmet Sezer",targetNode="Özge Nayır") #Add Özhe Nayır to Ahmet Sezer's friend list.
SNA.addRelation("Melis Alan","Zeynep Hat")
SNA.addRelation("Melis Alan","Faik Özsoy")
SNA.addRelation("Faik Özsoy","Ahmet Sezer")
SNA.addRelation("Faik Özsoy","Ahmet Sezer") #Gives Error message
SNA.addRelation("Ali Demir","Büşra Geçer") #Also it gives Error message, too.
SNA.removeRelation("Ali Demir","Büşra Geçer")
SNA.removeRelation("Melis Alan","Büşra Geçer") #Gives Error message
#print(SNA.generateGraphCode()) #Prints dot code to screen
SNA.renderGraph() #Render and show graph in pdf format.
