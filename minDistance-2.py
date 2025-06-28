class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        DP = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if word1[i - 1] == word2[j - 1]:
                    DP[j][i] = DP[j - 1][i - 1] + 1
                else:
                    DP[j][i] = max(DP[j][i - 1], DP[j - 1][i])

        return len(word1) + len(word2) - 2 * DP[-1][-1]

# https://leetcode.cn/problems/delete-operation-for-two-strings/solutions/1015796/liang-ge-zi-fu-chuan-de-shan-chu-cao-zuo-14uw