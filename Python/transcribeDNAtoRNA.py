import math
import time

        
def transcribeDNAtoRNA(DNA):
    """ (str) -> (str)"""
    DNA = list(DNA)
    RNA = []
    for s in DNA:
        if s == "T":
            RNA.append("U")
        else:
            RNA.append(s)
    
    RNA = ''.join(RNA)
    return RNA
    
if __name__ == '__main__':

    start = time.time()
    result = transcribeDNAtoRNA("ATCG")
    end = time.time()
    elapsed = (end  - start)

    print "result %s returned after %s seconds." % (result, elapsed)
