def findKMer(gene, k):
    max_k_mer = []
    max_k_mer_val = 0
    dics = dict()
    
    if len(gene) == k:
        max_k_mer = gene
    for i in range(0, len(gene)- k+1):
        current_char = gene[i: i+k]
        if current_char in dics:
            dics[current_char] = dics[current_char] + 1
        else:
            dics[current_char] = 1
    for kmer in dics:
        if dics[kmer] > max_k_mer_val:
            max_k_mer = []
            max_k_mer.append(kmer)
            max_k_mer_val = dics[kmer]
        elif dics[kmer] == max_k_mer_val:
            max_k_mer.append(kmer)
    return max_k_mer

gene = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
print(findKMer(gene, 3))
