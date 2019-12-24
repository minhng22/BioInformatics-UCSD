#Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
#Output: All most frequent k-mers with up to d mismatches in Text.

from neighborhood import find_neighborhood


def frequent_kmer_mismatch(text, k, d):
    frequent_patterns = []
    neighborhoods = dict()
    for i in range(len(text) - k):
        for n in find_neighborhood(text[i:i + k], d):
            if n in neighborhoods:
                neighborhoods[n] = neighborhoods[n] + 1
            else:
                neighborhoods[n] = 1
    max_occ = 0
    for n in neighborhoods:
        if neighborhoods[n] > max_occ:
            max_occ = neighborhoods[n]
    for n in neighborhoods:
        if neighborhoods[n] == max_occ:
            frequent_patterns.append(n)
    return len(frequent_patterns)
