from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        def possible(mid):
            for i in range(len(nums)):
                j = i + mid - 1
                if j < len(nums) and nums[j] - nums[i] <= 2 * k:
                    return True
            return False

        left, right = 1, len(nums)
        ans = 1
        while left <= right:
            m = (left + right) // 2
            if possible(m):
                ans = m
                left = m + 1
            else:
                right = m - 1
        return ans