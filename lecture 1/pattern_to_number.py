# sub and pattern is the same notation
def frequencyArray(gene, k):
    frequency_arr = dict()
    for i in range(0, len(gene)- k+1):
        current_char = gene[i: i+k]
        if current_char in frequency_arr:
            frequency_arr[current_char] = frequency_arr[current_char] + 1
        else:
            frequency_arr[current_char] = 1
    sorted_lst = sorted(frequency_arr.keys())
    return { i : sorted_lst[i] for i in range(0, len(sorted_lst) ) }

def patternToNumber(gene, sub):
    sorted_frequency_arr = frequencyArray(gene, len(sub))
    for key in sorted_frequency_arr:
        print(sorted_frequency_arr[key] , end =" ") 

print(patternToNumber('AAGCAAAGGTGGG', 'GT'))
