def arrayManipulation(n, queries):
    arr = [0] * (n + 2)
    for query in queries:
        arr[query[0]] += query[2]
        arr[query[1] + 1] -= query[2]

    S = 0
    dummy = 0
    for val in arr:
        dummy += val
        S = max(S, dummy)

    return S