#Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches
from approximate_occurance import approximateOccurance
def frequentWordMismatch (p,t,d):
    occurance = approximateOccurance(p,t,d)
    return len(occurance)

#testing
#p = 'TCCCCA'
#t = 'CGTGGGACTTCGAAAAAGTGTCTACCGACTCATTAGAGACGATGAGCTTGCTAACAAAGCTTCGCCCACAGCAGATCAACATGTAACTGTTTTATCCCTCGAGCGGCGAGATTGTGAGGCCCAGACCTCGTTGAGGTACAGCTATGAGTGCATGACGCAGACTGGGTTAGGAAGGATTGGCTGGGGTCGGTGGGGCTCGTCCCCACATCAGTGTGCCGATGCTTTCTAACACCTCACTGGTCTATGGATGCTATAGTAGGGGGTAAAGATCGCGTCAAATAGTCCCGCCCCCCATGGTCCTCCGTCAA'
#d = 3
#print(frequentWordMismatch(p,t,d))
