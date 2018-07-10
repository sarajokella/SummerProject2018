#! /usr/bin/env python

import os
import sys
import shutil
from ROOT import *
from histbins2 import binboundaries
from replacement import process, dict 

###############Variables to change##################################################

g = int(5) #NUMBER OF DESIRED BINS
variable = "nTracks" #DESIRED VARIABLE TO ANALYSE
number = "-1" #NUMBER OF EVENTS TO RUN OVER, DEFAULT "-1" IS ALL EVENTS
path = "../../builddir/" #PATH TO THE EPM

#ROOT FILE
file = TFile.Open("/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root")
f = file.Get("Bu2JpsiKplusDetached;1.root")
tree = f.Get("DecayTree;2")
#tree.Draw("nTracks>>h1")
tree.Draw(variable + ">>h1")

####################################################################################

word = ["even", "odd", "even"]
selection = ["&&eventNumber%2==0", "&&eventNumber%2!=0", "&&eventNumber%2==0"]
paths = path + "bin/SimpleEvaluator result.py 2>&1 | tee out.log" 
                       
for n in range(0,g):      
        for t in range(0,2):
                x = "Calib_Bin_"+ str(n) + "_" + word[t]
                y = "Comb_Bin_" + str(n) + "_" + word[t+1]
        
                if not os.path.exists(x):
                        os.makedirs(x) #make directories
                        os.makedirs(y)
                        bins = binboundaries(h1,g) #determine bin boundaries
                        j = """ " """
                        b = j[1]+ str(bins[n]) + "<=" + variable + "&&" + variable + "<" + str(bins[n+1]) + selection[t] + j[1]
                
                        dic = dict(number, b, "", "#", "test")         
                        process("EPMoptsTemplate.py", "result.py", dic) #create option file
                        shutil.move("result.py", os.path.join(x)) #move option file into correct directory
                        os.chdir(x)
                        #First Run of the EPM
                        os.system(paths) #calibration
                        os.chdir("..")
                        c = j[1] + str(bins[n]) +"<=" + variable + "&&" + variable + "<" + str(bins[n+1]) + selection[t+1] + j[1]
                        dic2 = dict(number, c, "#", "", x)
                        process("EPMoptsTemplate.py", "result.py", dic2)
                        shutil.move("result.py", os.path.join(y))
                        os.chdir(y)
                        #Second Run of the EPM
                        os.system(paths) #combination
                        os.chdir("../")
                else:  
                        print "subdirectory already exists!"
        


