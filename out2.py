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

        y = re.compile(r"Combination.*").search(s).group()

        final = list(map(float, re.findall(r'\d+\.\d+',y)))
        b = open("tagvalue.py", "a+")
        b.write('%s\n' % final[7:])
        return final    


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

#print re.compile(r"Tagger.*").search(s).group()
#prPurple(x)

#b = open("tagvalue.py", "a+")
#b.write(final)      
