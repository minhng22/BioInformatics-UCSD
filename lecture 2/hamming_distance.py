# Output: The Hamming distance between these strings.
def hamming_distance(p, q):
    h = 0
    for i in range(min(len(p),len(q))):
        if p[i] != q[i]:
            h += 1
    return h
