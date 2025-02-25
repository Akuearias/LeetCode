import collections
from typing import Collection


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        S = 0
        while i < len(s):
            C = 0
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if j+1 < len(s) and not sub.__contains__(s[j+1]):
                    C += 1
                    S = max(S, C)
                else:
                    break
            i += 1
        return S

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ab"))