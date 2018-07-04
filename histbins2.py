#! /usr/bin/env python

from ROOT import *
from array import array

def binboundaries(h1, nbins):
        
        cdf = h1.GetCumulative()
        cdf.Scale(1. / cdf.GetMaximum())
        if 1. != cdf.GetMaximum():
                raise "Problem with normalization"
        
        list = [cdf.GetXaxis().GetBinLowEdge(1)]
        n = 1
        for bin in xrange(1, cdf.GetNbinsX()):
                y = float(n) / float(nbins) # 1/N, 2/N,... N/N
                if y < cdf.GetBinContent(bin):
                        #slope dy is the upper edge of bin - lower edge of bin
                        dy = ((cdf.GetBinContent(bin) - cdf.GetBinContent(bin-1)) / (cdf.GetXaxis().GetBinUpEdge(bin) - cdf.GetXaxis().GetBinLowEdge(bin)))
                        x = cdf.GetXaxis().GetBinLowEdge(bin) + (y - cdf.GetBinContent(bin-1)) / dy
                        list.append(x)
                        n = n + 1
        list.append(cdf.GetXaxis().GetBinUpEdge(cdf.GetNbinsX())) #adds last bin
        return list

#upload the data from the root file
x = TFile.Open("/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root")
f = x.Get("Bu2JpsiKplusDetached;1.root")
tree = f.Get("DecayTree;2")
tree.Draw("nTracks>>h1")

#list = binboundaries(h1, 10) #print list of bin boundaries
#print list

#bin = array('d', list)
#h1.Rebin(len(bin)-1, "h2", bin)

#c1 = TCanvas('c1', 'Example', 200, 10, 1500, 1000) #create canvas
#c1.Divide(1,3)
#cdf = h1.GetCumulative()
#cdf.Scale(1. / cdf.GetMaximum()) #normalize cdf

#c1.cd(1)
#h1.Draw()
#c1.cd(2)
#cdf.Draw()
#c1.cd(3)
#h2.Draw()
#c1.cd(2)
#cdf.Draw()
#c1.Update()
#c1.Print("test2.png")
