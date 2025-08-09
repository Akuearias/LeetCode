from typing import List
import math


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]

        S = [[math.inf for _ in range(n)] for _ in range(m)]
        S[0][0] = grid[0][0]
        for i in range(1, n):
            S[0][i] = S[0][i - 1] + grid[0][i]
        for i in range(1, m):
            S[i][0] = S[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                S[i][j] = min(S[i - 1][j], S[i][j - 1]) + grid[i][j]

        return S[-1][-1]