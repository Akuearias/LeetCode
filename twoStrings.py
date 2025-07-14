import collections


def twoStrings(s1, s2):
    s1_counter, s2_counter = dict(collections.Counter(s1)), dict(collections.Counter(s2))
    for char in s1_counter:
        if char in s2_counter:
            return 'YES'
    return 'NO'