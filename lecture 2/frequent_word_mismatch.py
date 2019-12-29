#Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches
from approximate_occurance import approximate_occurrence
def frequent_word_mismatch (p: str, t: str, d: int):
    occurance = approximate_occurrence(p, t, d)
    return len(occurance)

#testing
#p = 'TCCCCA'
#t = 'CGTGGGACTTCGAAAAAGTGTCTACCGACTCATTAGAGACGATGAGCTTGCTAACAAAGCTTCGCCCACAGCAGATCAACATGTAACTGTTTTATCCCTCGAGCGGCGAGATTGTGAGGCCCAGACCTCGTTGAGGTACAGCTATGAGTGCATGACGCAGACTGGGTTAGGAAGGATTGGCTGGGGTCGGTGGGGCTCGTCCCCACATCAGTGTGCCGATGCTTTCTAACACCTCACTGGTCTATGGATGCTATAGTAGGGGGTAAAGATCGCGTCAAATAGTCCCGCCCCCCATGGTCCTCCGTCAA'
#d = 3
#print(frequentWordMismatch(p,t,d))
