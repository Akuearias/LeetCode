class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        DP = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            DP[i][0] = i
        for j in range(n + 1):
            DP[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    DP[i + 1][j + 1] = DP[i][j]
                else:
                    DP[i + 1][j + 1] = min(DP[i + 1][j] + 1, DP[i][j + 1] + 1, DP[i][j] + 1)

        return DP[-1][-1]
