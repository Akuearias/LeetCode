import bisect


def maximumSum(a, m):
    prefix = 0
    max_mod_sum = 0
    prefix_set = []

    for num in a:
        prefix = (prefix + num) % m
        max_mod_sum = max(max_mod_sum, prefix)

        i = bisect.bisect_right(prefix_set, prefix)
        if i < len(prefix_set):
            candidate = (prefix - prefix_set[i] + m) % m
            max_mod_sum = max(max_mod_sum, candidate)

        bisect.insort(prefix_set, prefix)

    return max_mod_sum