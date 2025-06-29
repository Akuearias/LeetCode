import math
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        DP = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            DP[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(n):
                L, R = math.inf, math.inf
                mid = DP[i - 1][j]
                if j - 1 >= 0:
                    L = DP[i - 1][j - 1]
                if j + 1 < n:
                    R = DP[i - 1][j + 1]
                DP[i][j] = matrix[i][j] + min(L, mid, R)

        return min(DP[-1])
