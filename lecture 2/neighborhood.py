#Implement Neighbors to find the d-neighborhood of a string.
#Input: A string Pattern and an integer d.
#Output: The collection of strings Neighbors(Pattern, d). (You may return the strings in any order, but each line should contain only one string.)

from hamming_distance import hamming_distance


def suffix_pattern(pattern) -> str:
    return pattern[1:]


def find_neighborhood(pattern: str, d: int) -> list:
    n = []
    if len(pattern) == 0:
        return
    if d == 0:
        n.append(pattern)
        return n
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    suffix_neighbors = find_neighborhood(suffix_pattern(pattern), d)
    for suffix_neighbor in suffix_neighbors:
        if hamming_distance(suffix_pattern(pattern), suffix_neighbor) < d:
            for nucleotide in ['A', 'T', 'G', 'C']:
                n.append(nucleotide + suffix_neighbor)
        else:
            n.append(pattern[0] + suffix_neighbor)
    return n


def find_neighborhood_dict(pattern: str, dics: dict, d: int) -> list:
    n = []
    if len(pattern) == 0:
        return
    if d == 0:
        n.append(pattern)
        return n
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    suffix_neighbors = find_neighborhood_dict(suffix_pattern(pattern), dics, d)
    for suffix_neighbor in suffix_neighbors:
        if hamming_distance(suffix_pattern(pattern), suffix_neighbor) < d:
            for nucleotide in ['A', 'T', 'G', 'C']:
                add_on = nucleotide + suffix_neighbor
                if add_on not in dics:
                    n.append(add_on)
        else:
            add_on = pattern[0] + suffix_neighbor
            if add_on not in dics:
                n.append(add_on)
    return n
