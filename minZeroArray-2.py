from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        nums2 = [{0} for _ in range(n)]
        if all(nums[i] in nums2[i] for i in range(n)):
            return 0

        for i, (L, R, v) in enumerate(queries):
            for j in range(L, R + 1):
                nums2[j] |= {s + v for s in nums2[j]}
            if all(nums[j] in nums2[j] for j in range(n)):
                return i + 1

        return -1
