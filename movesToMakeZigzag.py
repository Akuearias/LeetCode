from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        S1, S2 = 0, 0
        n = len(nums)
        for i in range(n):
            left = nums[i - 1] if i - 1 >= 0 else float('inf')
            right = nums[i + 1] if i + 1 < n else float('inf')
            min_neighbor = min(left, right)

            if i % 2 == 0:
                if nums[i] >= min_neighbor:
                    S2 += nums[i] - min_neighbor + 1
            else:
                if nums[i] >= min_neighbor:
                    S1 += nums[i] - min_neighbor + 1
        return min(S1, S2)
