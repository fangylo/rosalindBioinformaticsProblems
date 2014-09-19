import math
import time
import sys


## Question link:
## http://rosalind.info/problems/iprb/



def rabbitsRecurrenceRelations(month, pair):
    """ (int, int) -> (int)"""
    currentMature = 0;
    currentYoung = 1;
    
    nextMature = 0;
    nextYoung = 0;
    
    for m in range(1, month):
        nextMature = currentYoung + currentMature;
        nextYoung = currentMature* pair;
        
        currentMature = nextMature;
        currentYoung =nextYoung;
        print "month = " + str(m)
        print "current=" + str(currentMature+currentYoung)

    return  (currentMature+currentYoung)
    
if __name__ == '__main__':

    start = time.time()
    result = rabbitsRecurrenceRelations(28,2)
    end = time.time()
    elapsed = (end  - start)

    # print "result %s returned after %s seconds." % (result, elapsed)
    print result