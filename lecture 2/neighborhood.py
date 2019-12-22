#Implement Neighbors to find the d-neighborhood of a string.
#Input: A string Pattern and an integer d.
#Output: The collection of strings Neighbors(Pattern, d). (You may return the strings in any order, but each line should contain only one string.)

from hamming_distance import hammingDistance
def suffixPattern(pattern):
    return pattern[1:]
def findNeighborhood(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    n = []
    suffix_neighbors = findNeighborhood(suffixPattern(pattern), d)
    for suffix_neighbor in suffix_neighbors:
        if hammingDistance(suffixPattern(pattern), suffix_neighbor) < d:
            for nucleotide in ['A', 'T', 'G', 'C']:
                n.append(nucleotide + suffix_neighbor)
        else:
            n.append(pattern[0] + suffix_neighbor)
    return n

for key in findNeighborhood('ATT',2):
    print(key , end =" ")
