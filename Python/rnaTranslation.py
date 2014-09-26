import os
import math
import time
import sys


## Question link:
## http://rosalind.info/problems/prot/

def readSeq(seqFile):
    """ (FILE object) -> (str)"""
    line = seqFile.readline()
    seq = line.rstrip()
    return seq


def rnaCodonTable(codonFile):
    """ (FILE object) -> (dict)"""
    codonMap = {}
    line = codonFile.readline()    
    while line !="":  
        line = line.rstrip()
        key = line.split('\t')[0]
        aa = line.split('\t')[1]
        codonMap[key] = aa
        line = codonFile.readline()   
    return codonMap
    
def rnaTranslation(seq, codonMap):
    """ (str, dict) -> (str)"""
    
    aaSeq = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codonMap[codon] is 'Stop':
            break
        aaSeq.append(codonMap[codon])
    aaSeq = aaSeq[0:-1] # Get rid off the last list element ('Stop') 
    return aaSeq 
    
if __name__ == '__main__':

    with open("rosalind_prot.txt", 'r') as seqFile,open ("rnaCodon.txt",'r') as codonFile:
        codonMap = rnaCodonTable(codonFile)
        seq = readSeq(seqFile)
        aa = rnaTranslation(seq,codonMap)
        print ''.join(aa)


