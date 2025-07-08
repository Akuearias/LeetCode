import math


def hourglassSum(arr):
    max_ = -math.inf
    for i in range(4):
        for j in range(4):
            S = 0
            S += arr[i][j]
            S += arr[i][j+1]
            S += arr[i][j+2]
            S += arr[i+1][j+1]
            S += arr[i+2][j]
            S += arr[i+2][j+1]
            S += arr[i+2][j+2]
            max_ = max(max_, S)
    return max_
