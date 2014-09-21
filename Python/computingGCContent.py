from __future__ import division 
## http://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-in-python
import os
import math
import time
import sys
import operator

## Question link:
## http://rosalind.info/problems/gc/

class seqInfo:
    def __init__(self, line):
        """ (seqInfo, str) -> None type """
        # sequence string and GC content
        # line: string of DNA sequence
        self.seq = line;
        
        countA = 0;
        countC = 0;
        countG = 0;
        countT = 0;
        
        for n in list(line):
            if n == "A":
                countA = countA +1;
            elif n == "T" :
                countT = countT +1;
            elif n == "C" :
                countC = countC +1;
            elif n == "G":
                countG = countG +1;
            else:
                raise Exception ("Unknown DNA seq " + n )
        self.GC = (countC + countG)/ (countA+countT+countC + countG)
    
    def getGC(self):
        return self.GC
    
    def getSeq(self):
        return self.seq

        
def getSeqInfoFromFasta(FastaFILE):
    """ (File object) -> dict : key <str>, value <seqInfo>  """
    line = FastaFILE.readline()
    seqInfoDict={}
    
    while (line.startswith('>')!= True and line != ""):
        line = FastaFILE.readline()
    while line !="":        
        line = line.rstrip()
        seq_name = line[1:]
        # print "seq_name=" + seq_name 

        ### read next line which is sequence:
        seq = ''
        line = FastaFILE.readline()
        # line = line.rstrip('\n\r')

        while (line.startswith('>')!= True and line != ""):   
            line = line.rstrip()
            seq = seq + line                               
            line = FastaFILE.readline()  
        # print "seq_name=" + seq_name        
        # print "seq=" + seq    
        seqInfoDict[seq_name] = seqInfo(seq)
    return seqInfoDict


if __name__ == '__main__':

    fastaFileName = "rosalind_gc2.txt"
    
    with open(fastaFileName, 'r') as fastaFile:
        seqInfo = getSeqInfoFromFasta(fastaFile)
                
        GC={}
        for k in seqInfo:
            GC[k]=seqInfo[k].GC

        maxGCseqname =  max(GC.iteritems(), key=operator.itemgetter(1))[0]
        print maxGCseqname
        print seqInfo[maxGCseqname].GC*100
