class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            DP[i][0] = 1
        for j in range(n):
            DP[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1]

        return DP[-1][-1]