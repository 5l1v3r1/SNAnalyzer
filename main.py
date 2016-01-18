#!/usr/bin/env python3
import sna
SNA = sna.SNAnalyzer(inPath="example_network.txt",outPath="out/example_network.gv",engine="circo",analyzeType="tw")
SNA.renderGraph()
