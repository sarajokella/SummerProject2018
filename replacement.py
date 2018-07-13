#! /usr/bin/env python

import re
import os

def process(infile, outfile, dic): #function which reads in file and replaces key words with values from dictionary and writes to a new file
        
        if os.path.isfile(outfile) == True: #make sure you don't override any existing files
                raise NameError("Outfile already exists")

        with open(infile, "r") as a: 
                for line in a:
                        b = open(outfile, "a+")

                        if any(key in line for key in dic.keys()): #if a key exists in a line
                                for key, name in dic.iteritems(): #replace key with value
                                        if re.search(key,line):
                                                line = line.replace(key,name)
                                b.write(line)
                        else:                                           
                                b.write(line)           #else print line


def dict(t, u, v, w, x, y, z):                    #define the dictionairy
        dic = { "@@1@@" : t, #Nmax
                "@@2@@" : u, #Selection
                "@@3@@" : v, #XML Calibrations, must be off for run 2
                "@@4@@" : w, #Run 2 settings, commented during run 1
                "@@5@@" : x, #Path to XML Calibrations from run 1
                "@@6@@" : y, #Desired Root file
                "@@7@@" : z} #Decay Tree name
        return dic
