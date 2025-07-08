import collections

# Complete the freqQuery function below.
def freqQuery(queries):
    S = []
    dic = collections.defaultdict(int)
    freq = collections.defaultdict(int)

    for query in queries:
        op, val = query

        if op == 1:
            old_freq = dic[val]
            dic[val] += 1
            new_freq = dic[val]

            freq[old_freq] -= 1
            freq[new_freq] += 1

        elif op == 2:
            if dic[val] > 0:
                old_freq = dic[val]
                dic[val] -= 1
                new_freq = dic[val]

                freq[old_freq] -= 1
                freq[new_freq] += 1

                if dic[val] == 0:
                    del dic[val]

        elif op == 3:
            S.append(1 if freq[val] > 0 else 0)

    return S