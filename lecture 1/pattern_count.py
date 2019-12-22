def patterCount(gene, sub):
    cnt = 0
    k = len(sub)
    for i in range(0, len(gene)- k+1):
        current_char = gene[i: i+k]
        if current_char == sub:
            cnt += 1
    return cnt

gene = 'ACTGTACGATGATGTGTGTCAAAG'
sub = 'TGT'
print(patterCount(gene, sub))
