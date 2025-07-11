def pairs(k, arr):
    S = 0
    arr.sort(reverse=True)
    i, j = 0, 1
    n = len(arr)
    while j < n:
        diff = arr[i] - arr[j]
        if diff == k:
            S += 1
            i += 1
            j += 1
        elif diff < k:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1

    return S