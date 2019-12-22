# since the difference between total of G and C is negative on half strand and positive on the other half
def deamination (g):
    dics = {
        'A': 0,
        'T': 0,
        'C': -1,
        'G': 1
    }
    return dics[g]

def minimumSkew(t):
    min_skew = []
    min_skew_val = 0
    current_skew_val = 0
    for i in range(len(t)):
        current_skew_val += deamination(t[i])
        if current_skew_val < min_skew_val:
            min_skew_val = current_skew_val
            min_skew.clear()
            min_skew.append(i+1)
        elif current_skew_val == min_skew_val:
            min_skew.append(i+1)
    return min_skew

t = 'GATACACTTCCCGAGTAGGTACTG'
print(minimumSkew(t))

