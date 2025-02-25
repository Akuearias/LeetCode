import collections


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2) or (len(word1) == len(word2) and collections.Counter(word1) != collections.Counter(word2)):
            return 0

        S = 0
        char_info = [0 for _ in range(26)]
        for char in word2:
            char_info[ord(char) - ord('a')] += 1

        for i in range(len(word2), len(word1) + 1):
            r = len(word1) + 1
            while

        return S


solution = Solution()
print(solution.validSubstringCount("dcbdcdccb", "cdd"))
