#a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches
#Input: Integers k and d, followed by a collection of strings Dna.
#Output: All (k, d)-motifs in Dna.
from neighborhood import find_neighborhood_dict
from frequent_word_mismatch import frequent_word_mismatch


def motif_enumeration(texts, k, d):
    patterns = dict()
    p_array = []
    for text in texts:
        for i in range(len(text) - k + 1):
            current_text = text[i: i+k]
            neighborhood_patterns = find_neighborhood_dict(current_text, patterns, d)
            for pattern in neighborhood_patterns:
                appear_in_all = True
                for t in texts:
                    if frequent_word_mismatch(pattern, t, d) == 0:
                        appear_in_all = False
                if appear_in_all:
                    patterns[pattern] = 1
    for p in patterns:
        p_array.append(p)
    return p_array
