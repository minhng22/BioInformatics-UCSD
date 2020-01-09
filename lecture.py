import sys
import math
import itertools

# Week 1


def find_clump(gene, k, L, t):
    gen_len = len(gene)
    frequency_arr = frequency_array(gene[0:L], k)
    for i in range(L+1, gen_len):
        current_char = gene[L+1-k, L+1]
        if current_char in frequency_arr:
            frequency_arr[current_char] = frequency_arr[current_char] +1
            frequency_arr[current_char] = 1


def comp_nucleotide(n):
    dics = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return dics[n]


def find_complement(gene):
    comp = ''
    for i in range (len(gene)-1, -1, -1):
        comp += comp_nucleotide(gene[i])
    return comp


def find_k_mer(gene, k):
    max_k_mer = []
    max_k_mer_val = 0
    dics = dict()

    if len(gene) == k:
        max_k_mer = gene
    for i in range(0, len(gene) - k + 1):
        current_char = gene[i: i + k]
        if current_char in dics:
            dics[current_char] = dics[current_char] + 1
        else:
            dics[current_char] = 1
    for k_mer in dics:
        if dics[k_mer] > max_k_mer_val:
            max_k_mer = []
            max_k_mer.append(k_mer)
            max_k_mer_val = dics[k_mer]
        elif dics[k_mer] == max_k_mer_val:
            max_k_mer.append(k_mer)
    return max_k_mer


# Input: Ex:
# gene = 'ACTGTACGATGATGTGTGTCAAAG'
# sub = 'TGT'
def patter_count(gene, sub):
    cnt = 0
    k = len(sub)
    for i in range(0, len(gene)- k+1):
        current_char = gene[i: i+k]
        if current_char == sub:
            cnt += 1
    return cnt


def find_pattern_matching(gene, sub):
    len_sub = len(sub)
    matches = []
    for i in range(0, len(gene)- len_sub +1):
        current_char = gene[i: i+ len_sub]
        if current_char == sub:
            matches.append(i)
    return matches


# sub and pattern is the same notation
def frequency_array(gene, k):
    frequency_arr = dict()
    for i in range(0, len(gene)- k+1):
        current_char = gene[i: i+k]
        if current_char in frequency_arr:
            frequency_arr[current_char] = frequency_arr[current_char] + 1
        else:
            frequency_arr[current_char] = 1
    sorted_lst = sorted(frequency_arr.keys())
    return { i : sorted_lst[i] for i in range(0, len(sorted_lst) ) }


def pattern_to_number(gene, sub):
    sorted_frequency_arr = frequency_array(gene, len(sub))
    for key in sorted_frequency_arr:
        print(sorted_frequency_arr[key], end=" ")

# Week 2


# since the difference between total of G and C is negative on half strand and positive on the other half
def de_amination(g):
    dics = {
        'A': 0,
        'T': 0,
        'C': -1,
        'G': 1
    }
    return dics[g]


def minimum_skew(t):
    min_skew = []
    min_skew_val = 0
    current_skew_val = 0
    for i in range(len(t)):
        current_skew_val += de_amination(t[i])
        if current_skew_val < min_skew_val:
            min_skew_val = current_skew_val
            min_skew.clear()
            min_skew.append(i+1)
        elif current_skew_val == min_skew_val:
            min_skew.append(i+1)
    return min_skew


# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
# Input: Strings Pattern and Text along with an integer d.
# Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
def approximate_occurrence(p: str, t: str, d: int) -> list:
    o = []
    for i in range(len(t) - len(p) + 1):
        if hamming_distance(p, t[i: i + len(p)]) <= d:
            o.append(i)
    return o


def approximate_occurrence_count(p: str, t: str, d: int) -> int:
    return len(approximate_occurrence(p, t, d))


# Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as
# the total number of occurrences of Pattern in Text with at most d mismatches
def frequent_word_mismatch (p: str, t: str, d: int):
    occurrence = approximate_occurrence(p, t, d)
    return len(occurrence)


# Input: Two DNA string. Ex: 'ACGT', 'AGCAGATCGATCGTA'
# Output: The Hamming distance between these strings.
def hamming_distance(p: str, q: str) -> int:
    h = 0
    for i in range(min(len(p),len(q))):
        if p[i] != q[i]:
            h += 1
    return h


# calculate minimum hamming distance between pattern and dna
def hamming_distance_pattern(pattern: str, dna: str) -> int:
    h_distance = sys.maxsize
    for i in range(len(dna) - len(pattern) + 1):
        h_distance = min(h_distance, hamming_distance(pattern, dna[i: i+len(pattern)]))
    return h_distance


# Input: Ex: ACGTATA
# Output: Ex: CGTATA
def suffix_pattern(pattern) -> str:
    return pattern[1:]


# Implement Neighbors to find the d-neighborhood of a string.
# Input: A string Pattern and an integer d.
# Output: The collection of strings Neighbors(Pattern, d).
#   (You may return the strings in any order, but each line should contain only one string.)
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


def all_combination(k: int, cs: list) -> list:
    if k == 0:
        return cs
    if len(cs) == 0:
        cs.extend(['A', 'C', 'G', 'T'])
    else:
        for i in range(len(cs)):
            cs.extend([cs[i] + 'T', cs[i] + 'G', cs[i] + 'C'])
            cs[i] += 'A'
    return all_combination(k - 1, cs)


# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
# Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
# Output: All most frequent k-mers with up to d mismatches in Text.
def frequent_k_mer_mismatch(text, k, d):
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
    return frequent_patterns

# Week 3


# Input: An integer k, followed by a collection of strings Dna. Format of input is string separated by blank space
# Ex: 'ACGT AGGG ACTG', 3
# Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers.
#   (If there are multiple such strings Pattern, then you may return any one.)
def find_med_str_from_motif(texts: str, k: int) -> list:
    h_distance = sys.maxsize
    median = []
    for c in all_combination(k, []):
        if h_distance > pattern_and_string_distance(c, texts):
            h_distance = pattern_and_string_distance(c, texts)
            median.clear()
            median.append(c)
        elif h_distance == pattern_and_string_distance(c, texts):
            median.append(c)
    return median


# a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches
# Input: Integers k and d, followed by a collection of strings Dna.
# Output: All (k, d)-motifs in Dna.
def motif_enumeration(texts, k, d):
    patterns = dict()
    p_array = []
    for text in texts:
        for i in range(len(text) - k + 1):
            current_text = text[i: i + k]
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


def motif_scoring(motifs: list) -> float:
    score = 0
    for i in range(len(motifs[0])):
        local_score = 0
        prob = dict()
        prob['A'] = 0
        prob['C'] = 0
        prob['G'] = 0
        prob['T'] = 0
        for j in motifs:
            prob[j[i]] += 1
        max_appearance = 0
        total_appearance = 0
        for letter in ['A', 'C', 'G', 'T']:
            total_appearance += prob[letter]
            if max_appearance < prob[letter]:
                max_appearance = prob[letter]
        local_score = total_appearance - max_appearance
    score += local_score
    return score


# find entropy of list of integer
def list_entropy(values: list) -> float:
    total_entropy = 0
    for value in values:
        if value > 0:
            total_entropy += abs(value * math.log(value, 2))
        else:
            continue
    return total_entropy


def motif_matrix_entropy(motifs: list) -> float:
    profile = {}
    # check that all motifs are the same length
    list_length = len(motifs)
    l1 = len(motifs[1])  # length of the first motif
    nuc_dict = 'ACGT'

    for i in range(len(motifs)):
        if len(motifs[i]) != l1:
            short_motif = motifs[i]
            short_motif_len = len(short_motif)
            print('Oops, Motif {} is {} nucleotides instead of {}!'.format(short_motif, short_motif_len, l1))
            break

    # fill all positions with frequency of 0
    for nucleotide in nuc_dict:
        values = [0] * l1
        profile[nucleotide] = values

    # iterate through each position in the motif matrix, counting nucleotide frequencies
    total_entropy = 0
    for key, values in profile.items():
        for motif in motifs:
            for i in range(len(motif)):
                if motif[i] == key:
                    profile[key][i] += 1

        # convert nucleotide frequencies to probabilities
        for i in range(len(values)):
            profile[key][i] = profile[key][i] / float(list_length)

        # calculate total entropy (Sum of (Prob_value * log2 Prob_n))
        total_entropy += list_entropy(values)

    return total_entropy


def pattern_and_string_distance(pattern: str, dna: str) -> int:
    dna_list = dna.split(' ')
    total_h_distance = 0
    for dna in dna_list:
        total_h_distance += hamming_distance_pattern(pattern, dna)
    return total_h_distance


# Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
# Input: A string Text, an integer k, and a 4 × k matrix Profile.
# Output: A Profile-most probable k-mer in Text.
def two_d_array_to_matrix(profiles: list) -> dict():
    profile_arr = dict()
    profile_arr['A'] = profiles[0]
    profile_arr['C'] = profiles[1]
    profile_arr['G'] = profiles[2]
    profile_arr['T'] = profiles[3]
    return profile_arr


def profile_most_probable_kmer_problem(text: str, k: int, profiles: list) -> str:
    max_k_mer_val = 0
    max_k_mer = ""
    profile_arr = two_d_array_to_matrix(profiles)

    for j in range(len(text) - k + 1):
        k_mer = text[j: j + k]
        pr = 1
        for c in range(len(k_mer)):
            pr *= profile_arr[k_mer[c]][c]
        if max_k_mer_val < pr:
            max_k_mer_val = pr
            max_k_mer = k_mer
    return max_k_mer


# Input: Ex:
# profile = {
#     'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
#     'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
#     'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
#     'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
# }, k-mer = 'TCGGGGATTTCC'
def profile_probability(k_mer: str, profile: dict) -> float:
    prob = 1
    for i in range(len(k_mer)):
        letter = k_mer[i]
        prob *= profile[letter][i]
    return prob


# Input: A dictionary of occurrence. Ex:
# profile = {
#         'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
#         'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
#         'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
#         'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
# }
# Output: A list of consensus string
def find_consensus_str(profile: dict) -> list:
    length = len(profile['A'])
    c_matrices = []
    for i in range(length):
        c_val = []
        c = 0
        for letter in ['A', 'C', 'G', 'T']:
            if c < profile[letter][i]:
                c = profile[letter][i]
                c_val.clear()
                c_val.append(letter)
            elif c == profile[letter][i]:
                c_val.append(letter)
        c_matrices.append(c_val)
    c_matrices = list(itertools.product(*c_matrices))
    temp = c_matrices.copy()
    c_matrices.clear()
    for c_matrix in temp:
        dna = ''
        for letter in c_matrix:
            dna += letter
        c_matrices.append(dna)
    return c_matrices

# Week 4


# Implement RandomizedMotifSearch.
#
# Input: Integers k and t, followed by a collection of strings Dna.
# Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times.
#   Remember to use pseudocounts!
# Sample Input:
# 8 5
# CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
# GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
# TAGTACCGAGACCGAAAGAAGTATACAGGCGT
# TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
# AATCCACCAGCTCCACGTGCAATGTTGGCCTA
# Sample Output:
# TCTCGGGG
# CCAAGGTG
# TACAGGCG
# TTCAGGTG
# TCCACGTG
def randomized_motif_research(k: int, t: int, dna: list) -> list:
    motif = random_motif(dna)
    best_motif = motif
    looping = True
    while looping:
        profile = profile_most_probable_kmer_problem(motif)
        motif = motif(profile, dna)
        if motif_scoring(motif) < motif_scoring(best_motif):
            best_motif = motif
        elif motif_scoring(motif) == motif_scoring(best_motif):
            looping = False
    return best_motif


def random_motif(dna: list) -> str: