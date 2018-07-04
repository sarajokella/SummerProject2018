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

def dict(x, y, z):                    #define the dictionairy
        dic = { "@@1@@" : x,
                "@@2@@" : y,
                "@@3@@" : z}
        return dic
                
#dic = dict("50000",'"' + '"', "1") # first argument is how to add double quotes as a string

#process("EPMoptsTemplate.py", "result.py", dic)
