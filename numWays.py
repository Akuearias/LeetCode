import collections
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        frequencies = [collections.Counter() for _ in range(len(words[0]))]
        for word in words:
            for i in range(len(word)):
                frequencies[i][word[i]] += 1

        DP = [0] * (len(target) + 1)
        DP[0] = 1
        for i in range(len(words[0])):
            for j in range(len(target) - 1, -1, -1):
                DP[j + 1] = (DP[j + 1] + frequencies[i][target[j]] * DP[j]) % (10 ** 9 + 7)

        return DP[-1]



