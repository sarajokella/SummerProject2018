#! /usr/bin/env python

import os
import sys
import shutil
from ROOT import *
from histbins2 import binboundaries
from replacement import process, dict 

###############Variables to change##################################################

g = 5 #NUMBER OF DESIRED BINS
variable = "nTracks" #DESIRED VARIABLE TO ANALYSE
number = "-1" #NUMBER OF EVENTS TO RUN OVER, DEFAULT "-1" IS ALL EVENTS
path = "../../builddir/" #PATH TO THE EPM FROM WHERE JOB.PY IS RUN
root = "/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root" #DESIRED ROOT FILE
trees = "Bu2JpsiKplusDetached" #DECAY TREE

###################################################################################

#ROOT FILE
file = TFile.Open(root)
f = file.Get(trees + ";1.root")
tree = f.Get("DecayTree;2")
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
                        b = str(bins[n]) + "<=" + variable + "&&" + variable + "<" + str(bins[n+1]) + selection[t]
                
                        dic = dict(number, b, "", "#", "test", root, trees + "/DecayTree")         
                        process("EPMoptsTemplate.py", "result.py", dic) #create option file for 1st run
                        shutil.move("result.py", os.path.join(x)) #move option file into correct directory
                        os.chdir(x)
     
                        #First Run of the EPM
                        os.system(paths) #calibration
                        os.chdir("..")
                        c = str(bins[n]) +"<=" + variable + "&&" + variable + "<" + str(bins[n+1]) + selection[t+1] #opt file for 2nd run
                        dic2 = dict(number, c, "#", "", x, root, trees + "/DecayTree")
                        process("EPMoptsTemplate.py", "result.py", dic2)
                        shutil.move("result.py", os.path.join(y))
                        os.chdir(y)
     
                        #Second Run of the EPM
                        os.system(paths) #combination
                        os.chdir("../")
                else:  
                        print "subdirectory already exists!"
        


