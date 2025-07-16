import math


def maxMin(k, arr):
    arr.sort()
    i = 0
    S = math.inf
    while i < len(arr) - k + 1:
        S = min(S, arr[i + k - 1] - arr[i])
        i += 1
    return S