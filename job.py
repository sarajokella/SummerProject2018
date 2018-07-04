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
#bins =  binboundaries(h1, 10)

from replacement import process, dict 
                       
for n in range(0,5):      
        
        #user_input = raw_input("Enter subdirectory name: ")
        x = "Calib_Bin_"+ str(n)
        y = "Comb_Bin_" + str(n)
        
        if not os.path.exists(x):
                os.makedirs(x) #make directories
                os.makedirs(y)
                bins = binboundaries(h1,5) #determine bin boundaries
                j = """ " """
                b = j[1]+ str(bins[n]) +"<=nTracks&&nTracks<" + str(bins[n+1])+j[1] 
                
                dic = dict("50000", b, "1")         
                process("EPMoptsTemplate.py", "result.py", dic) #create option file
                shutil.move("result.py", os.path.join(x)) #move option file into correct directory
                os.chdir(x)
                os.system(r"../../builddir/bin/SimpleEvaluator result.py 2>&1 | tee out.log") #calibration
                shutil.move("EspressoCalibrations.py", os.path.join('..',y))
                shutil.move("result.py", os.path.join('..',y))
                os.chdir(os.path.join("..",y))
                os.system(r"../../builddir/bin/SimpleEvaluator result.py EspressoCalibrations.py 2>&1 | tee out.log") #combination
                os.chdir("../")
        else:  
                print "subdirectory already exists!"
        


