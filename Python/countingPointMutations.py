import os
import math
import time
import sys


## Question link:
## http://rosalind.info/problems/hamm/

def readSeq(seqFile):
    """ (FILE object) -> (str,str)"""
    line = seqFile.readline()
    seq1 = line.rstrip()
    line = seqFile.readline()
    seq2 = line.rstrip()
    return (seq1, seq2)
    
def countingPointMutations(seq1, seq2):
    """ (str, str) -> int"""
    seqLength = len(list(seq1))
    
    hammingDistance=0;
    for i in range(0,seqLength):
        if list(seq1)[i]!=list(seq2)[i]:
            hammingDistance = hammingDistance+1;
    return hammingDistance

if __name__ == '__main__':

    FILE = "text.txt"
    
    with open(FILE, 'r') as seqFile:
        seq1, seq2 = readSeq(seqFile)
        # print seq1
        # print seq2
        print countingPointMutations(seq1, seq2)
