import collections
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        word = strs[0]
        new_strs = strs[1:]
        for i in range(1, len(word)+1):
            for j in range(len(new_strs)):
                if new_strs[j][0:i] != word[0:i]:
                    break
                elif j + 1 == len(new_strs):
                    prefix = new_strs[j][0:i]
        return prefix


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flower", "flower"]))
