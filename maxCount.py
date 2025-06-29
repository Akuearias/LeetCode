from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        S = 0
        T = 0
        for i in range(1, n + 1):
            if i not in banned_set and T + i <= maxSum:
                T += i
                S += 1
            if T > maxSum:
                break
        return S

