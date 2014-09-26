from __future__ import division
import math
import time
import sys
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

## Question link:
## http://rosalind.info/problems/iprb/

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )


def mendelFirstLaw(homDom,het,homRec):
    """ (int, int, int) -> (float)"""
    total = homDom + het + homRec
    a = 4*nCk(homRec,2) + 2*nCk(het,1)*nCk(homRec,1)+1*nCk(het,2)
    b = 4*(nCk(total,2))
    
    return  1-(a/b)
    
if __name__ == '__main__':

    start = time.time()
    result = mendelFirstLaw(24,30,15)
    end = time.time()
    elapsed = (end  - start)

    # print "result %s returned after %s seconds." % (result, elapsed)
    print result
