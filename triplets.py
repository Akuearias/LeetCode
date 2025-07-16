import bisect


def triplets(a, b, c):
    set_a, set_b, set_c = sorted(set(a)), sorted(set(b)), sorted(set(c))

    S = 0
    for num in set_b:
        S1 = bisect.bisect_right(set_a, num)
        S2 = bisect.bisect_right(set_c, num)
        S += S1 * S2

    return S