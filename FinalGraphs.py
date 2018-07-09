#! /usr/bin/env python

from ROOT import *
import os
import shutil
from out2 import values
from histbins2 import binboundaries
import math
       
tago = [0]*5
tage = [0]*5
yerrorse = [0]*5
yerrorso = [0]*5
xerrors = [0]*5
bins = [0]*5

file = TFile.Open("/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root")
f = file.Get("Bu2JpsiKplusDetached;1.root")
tree = f.Get("DecayTree;2")
tree.Draw("nTracks>>h1")


for n in range(0,5):
        bins[n] = (binboundaries(h1,5)[n+1] + binboundaries(h1,5)[n])/2 #find halfway point between bin boundaries
        x = "Comb_Bin_" + str(n) + "_even"
        y = "Comb_Bin_" + str(n) + "_odd"
        shutil.move("out2.py", os.path.join(x)) #out2.py is the script that extracts the tagging power information
        os.chdir(x) 
        tage[n] = values("out.log")[7] #tagging power for even directories
        yerrorse[n] = math.sqrt(values("out.log")[8]**2 + values("out.log")[9]**2) #extracts y errors
        xerrors[n] = (binboundaries(h1,5)[n+1] - binboundaries(h1,5)[n])/2 # finds x errors
        shutil.move("out2.py", os.path.join("..",y))
        os.chdir(os.path.join("..",y))
        tago[n] = values("out.log")[7] #tagging power for odd directories
        yerrorso[n] = math.sqrt(values("out.log")[8]**2 + values("out.log")[9]**2)
        shutil.move("out2.py", "..")
        os.chdir("..")

c = TCanvas('c1', 'Final Graph', 200, 10, 1800, 1000)
c.Divide(2,1)
c.cd()

cbins = ROOT.std.vector("double")() #converts python list into vectors that Root can process
ctage = ROOT.std.vector("double")()
ctago = ROOT.std.vector("double")()
cyerrorse = ROOT.std.vector("double")()
cyerrorso = ROOT.std.vector("double")()
cxerrors = ROOT.std.vector("double")()

for i in bins:
        cbins.push_back(i)
for i in tago:
        ctago.push_back(i)
for i in tage:
        ctage.push_back(i)
for i in yerrorse:
        cyerrorse.push_back(i)
for i in yerrorso:
        cyerrorso.push_back(i)
for i in xerrors:
        cxerrors.push_back(i)

g2 = TGraphErrors(5, cbins.data(), ctage.data(), cxerrors.data(), cyerrorse.data())
g3 = TGraphErrors(5, cbins.data(), ctago.data(), cxerrors.data(), cyerrorso.data()) 

c.cd(1)
g2.SetTitle("Even Events")
g2.GetXaxis().SetTitle("N Tracks")
g2.GetYaxis().SetTitle("Effective Tagging Power (%)")
g2.Draw("AP")
c.cd(2)
g3.SetTitle("Odd Events")
g3.GetXaxis().SetTitle("N Tracks")
g3.GetYaxis().SetTitle("Effective Tagging Power (%)")
g3.Draw("AP")
c.Print("FinalGraph.png")
