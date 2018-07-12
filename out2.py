#! /usr/bin/env python

#print out the values for the combination calibrated tagging performances

import re

def values(x):

        with open(x,"r") as f:      
                for line in f:
                        if re.compile(r"CALIBRATED TAGGING").search(line, re.M) != None:
                                start = line
                        if  re.compile(r"HISTOGRAMS").search(line, re.M) != None:
                                end = line
                        
        f = open(x, "r")    
        file = f.read()
        f.close()
        s = file[(file.index(start)+len(start)):file.index(end)]

        y = re.compile(r"\sCombination.*").search(s).group() #Combination can be changed to a tagger value

        final = list(map(float, re.findall(r'\d+\.\d+',y))) #create list of combination tagging performance values from out.log file
        return final    


# the final list contains the 10 numbers from the Calibrated Tagging Performance table in the out.log file
