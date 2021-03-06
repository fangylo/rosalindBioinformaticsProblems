import math
import time

# QUestion link:http://rosalind.info/problems/revc/
        
def complementDNA(seq):
    """ (str) -> (str)"""
    seq = list(seq)
    compliment_seq = []
    for s in seq:
        if s == "A":
            compliment_seq.append("T")
        elif s == "T" :
            compliment_seq.append("A")
        elif s == "C" :
            compliment_seq.append("G")
        elif s == "G":
            compliment_seq.append("C")
    
    compliment_seq = ''.join(compliment_seq)
    return compliment_seq[::-1]
    
if __name__ == '__main__':

    start = time.time()
    result = complementDNA("TACAAACAGTTTTGTTCCCGTGCACTTTCTTGGCCGCGTGGGTCGATCGACAAACATAGACAGCGTGATTACCGTAAAAACACTCTCGAAGCTGACATGACAGCGAGCCTCGTTGCACACGCGACTCAGCAGGGCGACCGCGTGTACCAAACAGGGTTACTTCCACTTGGCCGGTCACTCAGCCGTTAAAGTGTAACGTCGGGAAGTAGGGCAGTGCGCAGTATTCCTACGAACAGCCAACGGTGGGCAATTCAACTTCTCCATCTTAGGCAGGTGGTGCGTTACCTCAGTAAGGATACTGAAAACCTTGCAAATTGATGTGATGAATAATAACACCGCCTACTCAATTGCTGTTATATTGTGAGTTTTACTGTGTGCGCGTTGTGCCTCTGAAACATAAATAGCCGGCATTCGGATAACGAGCATGGCCAGCGAAAGCGCTCGCTCTGCCTATACAGGCTCGTTTGGAAAACGGCCCATAGTCGGAGGTGCAGGGTCAATGGGTTCTGAGGCTAAGATCGAATGACCGCTACAGTTAATTCGCGCCTTTGAAGTATTAGAAACCACCACGAACACAGTTCCTTCTCCATCACGAGCACGCGTTCGGAATTCTCTTACGCGCGTCTTTCTCGGCTAACGGACCCCGAAGGATTATGGGGCTGTTCCAAATCTGCCTCATATTCGAAACTGTCTAATTGCCTATTGGTGCGGCAGGCTGCGATGTGCGAGCCCGGGTCTTCAAGTTGATAATCGAGGACGTATGAGGGGATAGTAGGGATCGTTACCACTCGCCCTTTAGACTGTCTATCGGGAAGCGGAATTTTGAAGGCCCCCCTTCCCAGCATGCCACTATGTAAAGATACGCCTTTGGTGGAGAACGTTGTTCTGACGGTGAGCGAAACTATATGTTTCGCACGTACGCTAAAGCCA")
    end = time.time()
    elapsed = (end  - start)

    # print "result %s returned after %s seconds." % (result, elapsed)
    print result
