import math


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
        for value in values:
            if value > 0:
                total_entropy += abs(value * math.log(value, 2))
            else:
                continue

    return total_entropy
