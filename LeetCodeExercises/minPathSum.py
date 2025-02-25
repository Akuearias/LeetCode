import math
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        start = grid[0][0]
        x = 1
        y = 1
        L = len(grid) - 1
        W = len(grid[0]) - 1
        dp = [math.inf] * (L + W + 1)
        dp[1] = start
        i = 1
        while i <= L + W:
            dp[i] = min(dp[i], start + grid[x][0])
            i += 1


        return dp[-1]

solution = Solution()
print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
