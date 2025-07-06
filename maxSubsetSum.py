# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    DP = [0] * (1 + len(arr))
    DP[1] = max(0, arr[0])
    for i in range(1, len(arr)):
        DP[i + 1] = max(DP[i], DP[i - 1] + arr[i])
    return DP[-1]