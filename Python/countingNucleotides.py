import math
import time

## Question link:
## http://rosalind.info/problems/dna/
        
def countNucleotides(seq):
    """ (str) -> (str)"""
    seq = list(seq)
    countA = 0;
    countC = 0;
    countG = 0;
    countT = 0;
    
    for s in seq:
        if s == "A":
            countA = countA +1;
        elif s == "T" :
            countT = countT +1;
        elif s == "C" :
            countC = countC +1;
        elif s == "G":
            countG = countG +1;
        else:
            raise Exception ("Unknown DNA seq " + s )
    counts = [countA,countC,countG,countT]  
    counts = ' '.join(str(e) for e in counts)
    return  counts
    
if __name__ == '__main__':

    start = time.time()
    result = countNucleotides("ATCGG")
    end = time.time()
    elapsed = (end  - start)
    print result
    # print "result %s returned after %s seconds." % (result, elapsed)
