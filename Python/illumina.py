# import os
# import math
# import time
# import sys


def compareLines(baselineFile, testFile):
    baseline = baselineFile.readline()
    testline = testFile.readline()
    linecount = 1
    
    while baseline !="": 
        baseline = baseline.rstrip()
        testline = testline.strip()
        diff = (float(testline) - float(baseline))/float(baseline)
        diffPercentage = diff*100

        if baseline != testline and diff <0.05:
            print '[WARNING] '+ str(diffPercentage) +'% change detected on line '+str(linecount) + \
            '(baseline:'+ str(baseline) +', test:' + str(testline) +')'
        elif baseline != testline and diff >=0.05:
            print '[ERROR] '+ str(diffPercentage) +'% change detected on line '+str(linecount) + \
            '(baseline:'+ str(baseline) +', test:' + str(testline) +')'
        
        baseline = baselineFile.readline()
        testline = testFile.readline()
        linecount = linecount+1
        
if __name__ == '__main__':
        
    with open("baseline.txt", 'r') as baselineFile, open("test.txt",'r') as testFile,\
        open("output.txt",'w'):
       
        compareLines(baselineFile, testFile)