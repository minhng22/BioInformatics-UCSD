#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#Input: Strings Pattern and Text along with an integer d.
#Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

from hamming_distance import hamming_distance


def approximate_occurrence(p: str, t: str, d: int) -> list:
    o = []
    for i in range(len(t) - len(p) + 1):
        if hamming_distance(p, t[i: i + len(p)]) <= d:
            o.append(i)
    return o


def approximate_occurrence_count(p: str, t: str, d: int) -> int:
    return len(approximate_occurrence(p, t, d))
