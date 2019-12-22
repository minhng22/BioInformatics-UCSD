from pattern_to_number import frequencyArray
def findClump(gene, k, L, t):
    gen_len = len(gene)
    frequency_arr = frequencyArray(gene[0:L],k)
    for i in range(L+1, gen_len):
        current_char = gene[L+1-k, L+1]
        if current_char in frequency_arr:
            frequency_arr[current_char] = frequency_arr[current_char] +1
            frequency_arr[current_char] = 1
