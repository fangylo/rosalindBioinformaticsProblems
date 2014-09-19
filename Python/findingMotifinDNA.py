import math
import time
import regex as re
import sys

## Question link:
## http://rosalind.info/problems/subs/
        
def findingMotifinDNA(motif, DNAsequence):
    """ (str,str) -> (int,int)"""

    # matches = re.findall(motif, DNAsequence, overlapped=True)
    matches = re.finditer(motif, DNAsequence, overlapped=True)
    return  [match.start(0)+1 for match in matches]
    
if __name__ == '__main__':

    start = time.time()
    result = findingMotifinDNA("GCTAACAGC","GAGCTAACAGTATGCTAACACGTGCTAACAACGCTAACAGCTAACAGGGCTAACAGGGCTAACAGGCTAACAGCTAACAGCTAACAGTGCTAACAGCTAACAGCTAACAGCTAACAGGCTAACAGCGCTAACAGCTAACAGCTAACACCAGTGCTAACAGCTAACACCTGCTAACACGCTAACAGCTAACAGGGCCGCTAACAAAGCTAACACGCTAACAGCGCTAACAAGCTAACAGCTAACATCGCTAACATTTCTGGCTAACAGCTAACACAGGCCGCTAACAGGGCTAACAGCTAACAGTATGCTAACACGCTAACAATTGGCTAACACCGCTAACATAAAAATGCTAACAACGCTAACAGTGCTGCTAACAGGACGCCGCTAACACGTGGAGCTAACAGCTAACAAACCGCTCGGGCTAACAGCTAACAGCTAACAGCGGCTAACACGCTAACAGTGCTAACAGCTAACACATCGCTAACATTGCTAACATGCTAACAAGTGCTAACAGCTAACAGGCTAACAACTAATAGGCTAACAGCTAACAGCTAACACAGTAGGCTAACAACTATTATTATGCTAACAATGGCCATGCTAACAGCTAACAGCTAACAGCTAACACATGAGCTAACAGGCTGTTGCTAACAGCTAACAGCTAACATTGGGCTAACAACGATCGGGCTAACAGCTAACAGCTAACAGAGCTAACATCTCGTGCTAACAATGCCGCTAACATCGCTGGCTAACATGCTAACAGCTAACAGGGTAATTGCTAACACGGCTAACAAGCTAACAGCTAACATGGCTAACACTGCTAACAAGCTAACATGCTAACATACTCGCTAACAGTGCTAACAAAGCTAACAAGCTAACATGCTAACAGCTAACATCGCTAACATATGCTAACAAGCTAACAACGCTAACA")
    end = time.time()
    elapsed = (end  - start)

    # print "result %s returned after %s seconds." % (result, elapsed)
    print ' '.join(str(e) for e in result)