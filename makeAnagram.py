import collections


def makeAnagram(a, b):
    S = 0
    dic_a, dic_b = dict(collections.Counter(a)), dict(collections.Counter(b))
    for i in range(ord('a'), ord('z') + 1):
        S += abs(dic_a.get(chr(i), 0) - dic_b.get(chr(i), 0))
    return S