def candies(n, arr):
    if len(arr) == 1:
        return 1
    max_ = arr[0]
    DP = [1] * len(arr)
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            if arr[i] > max_:
                max_ = arr[i]
            DP[i] = DP[i - 1] + 1

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            DP[i] = max(DP[i + 1] + 1, DP[i])

    return sum(DP)