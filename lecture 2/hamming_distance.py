# Output: The Hamming distance between these strings.
def hammingDistance(p, q):
    h = 0
    for i in range(len(q)):
        if p[i] != q[i]:
            h += 1
    return h

# testing
p = 'CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
q= 'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'
print(hammingDistance(p,q))
