def minimumSwaps(arr):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        hashmap[arr[i]] = i
    S = 0
    i = 0
    while i < n:
        if arr[i] != i + 1:
            dummy1 = hashmap[i + 1]
            dummy2 = i
            hashmap[i + 1] = dummy2
            hashmap[arr[i]] = dummy1
            arr[i], arr[dummy1] = arr[dummy1], arr[i]
            S += 1
        i += 1
    return S