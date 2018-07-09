#! /usr/bin/env python

import os
import sys
import shutil
from ROOT import *
from histbins2 import binboundaries

file = TFile.Open("/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root")
f = file.Get("Bu2JpsiKplusDetached;1.root")
tree = f.Get("DecayTree;2")
tree.Draw("nTracks>>h1")

from replacement import process, dict 
word = ["even", "odd", "even"]
selection = ["&&eventNumber%2==0", "&&eventNumber%2!=0", "&&eventNumber%2==0"]
user_input = raw_input("Enter number of bin boundaries: ")
g = int(user_input)
                       
for n in range(0,g):      
        for t in range(0,2):
                x = "Calib_Bin_"+ str(n) + "_" + word[t]
                y = "Comb_Bin_" + str(n) + "_" + word[t+1]
        
                if not os.path.exists(x):
                        os.makedirs(x) #make directories
                        os.makedirs(y)
                        bins = binboundaries(h1,g) #determine bin boundaries
                        j = """ " """
                        b = j[1]+ str(bins[n]) +"<=nTracks&&nTracks<" + str(bins[n+1]) + selection[t] + j[1]
                
                        dic = dict("-1", b, "", "#", "test")         
                        process("EPMoptsTemplate.py", "result.py", dic) #create option file
                        shutil.move("result.py", os.path.join(x)) #move option file into correct directory
                        os.chdir(x)
                        #First Run of the EPM
                        os.system(r"../../builddir/bin/SimpleEvaluator result.py 2>&1 | tee out.log") #calibration
                        os.chdir("..")
                        c = j[1] + str(bins[n]) +"<=nTracks&&nTracks<" + str(bins[n+1]) + selection[t+1] + j[1]
                        dic2 = dict("-1", c, "#", "", x)
                        process("EPMoptsTemplate.py", "result2.py", dic2)
                        shutil.move("result2.py", os.path.join(y))
                        os.chdir(y)
                        #Second Run of the EPM
                        os.system(r"../../builddir/bin/SimpleEvaluator result2.py 2>&1 | tee out.log") #combination
                        os.chdir("../")
                else:  
                        print "subdirectory already exists!"
        


