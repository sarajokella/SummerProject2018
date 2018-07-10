#! /usr/bin/env python

from ROOT import *
import os
import shutil
from out2 import values
from histbins2 import binboundaries
import math
from operator import add, truediv, mul

m = 5 #NUMBER OF BINS
variable = "nTracks" #DESIRED VARIABLE TO ANALYSE

file = TFile.Open("/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root")
f = file.Get("Bu2JpsiKplusDetached;1.root")
tree = f.Get("DecayTree;2")
tree.Draw(variable + ">>h1")
       
tago = [0]*m
tage = [0]*m
yerrorse = [0]*m
yerrorso = [0]*m
xerrors = [0]*m
bins = [0]*m



for n in range(0,m):
        bins[n] = (binboundaries(h1,m)[n+1] + binboundaries(h1,m)[n])/2 #find halfway point between bin boundaries
        x = "Comb_Bin_" + str(n) + "_even"
        y = "Comb_Bin_" + str(n) + "_odd"
        shutil.move("out2.py", os.path.join(x)) #out2.py is the script that extracts the tagging power information
        os.chdir(x) 
        tage[n] = values("out.log")[7] #tagging power for even directories
        yerrorse[n] = math.sqrt(values("out.log")[8]**2 + values("out.log")[9]**2) #extracts y errors
        xerrors[n] = (binboundaries(h1,m)[n+1] - binboundaries(h1,m)[n])/2 # finds x errors
        shutil.move("out2.py", os.path.join("..",y))
        os.chdir(os.path.join("..",y))
        tago[n] = values("out.log")[7] #tagging power for odd directories
        yerrorso[n] = math.sqrt(values("out.log")[8]**2 + values("out.log")[9]**2)
        shutil.move("out2.py", "..")
        os.chdir("..")

ones = [1]*m #uses linear least-squares fitting to combine the even and odd events and the errors

k = map(truediv,tage,yerrorse)
l = map(truediv,tago,yerrorso)
final = map(truediv,map(add,k,l), map(add,map(truediv,ones,yerrorse),map(truediv,ones,yerrorso)))
yerror = map(truediv, map(mul,yerrorso,yerrorse), map(add,yerrorso,yerrorse))

c = TCanvas('c1', 'Final Graph', 200, 10, 1800, 1000) #create canvas to draw graph on

cbins = ROOT.std.vector("double")() #converts python list into vectors that Root can process
cfinal = ROOT.std.vector("double")()
cyerror = ROOT.std.vector("double")()
cxerrors = ROOT.std.vector("double")()

for i in bins:
        cbins.push_back(i)
for i in final:
        cfinal.push_back(i)
for i in yerror:
        cyerror.push_back(i)
for i in xerrors:
        cxerrors.push_back(i)

g2 = TGraphErrors(m, cbins.data(), cfinal.data(), cxerrors.data(), cyerror.data())

c.cd()
#g2.SetTitle("Even Events")
g2.GetXaxis().SetTitle("N Tracks")
g2.GetYaxis().SetTitle("Effective Tagging Power (%)")
g2.Draw("AP")
c.Print("FinalGraph.png")
