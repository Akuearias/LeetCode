from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        L, R = 0, arr[-1]
        while L < R:
            mid = (L + R) // 2
            S = 0
            for num in arr:
                S += min(num, mid)
            if S > target:
                R = mid
            elif S < target:
                L = mid + 1
            else:
                return mid

        S1, S2 = 0, 0
        for num in arr:
            S1 += min(num, L)
            S2 += min(num, L - 1)
        if abs(S2 - target) <= abs(S1 - target):
            return L - 1
        else:
            return L
