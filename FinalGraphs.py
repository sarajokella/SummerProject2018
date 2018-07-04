#! /usr/bin/env python

from ROOT import *
import os
import shutil
from out2 import values
from histbins2 import binboundaries
import math
       
tag = [0]*5
yerrors = [0]*5
xerrors = [0]*5
bins = [0]*5

file = TFile.Open("/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root")
f = file.Get("Bu2JpsiKplusDetached;1.root")
tree = f.Get("DecayTree;2")
tree.Draw("nTracks>>h1")

for n in range(0,5):
        bins[n] = (binboundaries(h1,5)[n+1] + binboundaries(h1,5)[n])/2
        x = "Comb_Bin" + str(n)
        y = "Comb_Bin" + str(n+1)
        shutil.move("out2.py", os.path.join(x))
        os.chdir(x) 
        tag[n] = values("out.log")[7]
        yerrors[n] = math.sqrt(values("out.log")[8]**2 + values("out.log")[9]**2)
        xerrors[n] = (binboundaries(h1,5)[n+1] - binboundaries(h1,5)[n])/2
        shutil.move("out2.py", "..")
        os.chdir("..")

c = TCanvas('c1', 'Final Graph', 200, 10, 1500, 1000)
c.cd()

cbins = ROOT.std.vector("double")()
ctag = ROOT.std.vector("double")()
cyerrors = ROOT.std.vector("double")()
cxerrors = ROOT.std.vector("double")()

for i in bins:
        cbins.push_back(i)
for i in tag:
        ctag.push_back(i)
for i in yerrors:
        cyerrors.push_back(i)
for i in xerrors:
        cxerrors.push_back(i)

g2 = TGraphErrors(5, cbins.data(), ctag.data(), cxerrors.data(), cyerrors.data())

#g1 = TGraphErrors(5)
#for i in range(1,6):
       # g1.SetPoint(i, bins[i-1], tag[i-1])

c.cd()
g2.GetXaxis().SetTitle("N Tracks")
g2.GetYaxis().SetTitle("Effective Tagging Power (%)")
g2.Draw("AP")
c.Print("FinalGraph.png")
