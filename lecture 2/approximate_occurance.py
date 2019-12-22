#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#Input: Strings Pattern and Text along with an integer d.
#Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

from hamming_distance import hammingDistance
def approximateOccurance(p, t, d):
    o = []
    for i in range(len(t)- len(p) + 1):
        if hammingDistance(p, t[i: i + len(p)]) <= d:
            o.append(i)
    return o

#testing

p = 'TGT'
t = 'CGTGACAGTGTATGGGCATCTTT'
d = 1

for key in approximateOccurance(p, t, d):
    print(key , end =" ")
