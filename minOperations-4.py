from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_ = sum(nums)
        if sum_ < x:
            return -1
        if sum_ == x:
            return len(nums)

        max_ = -1
        L = 0
        s = 0
        for R in range(len(nums)):
            s += nums[R]
            while s > sum_ - x and L <= R:
                s -= nums[L]
                L += 1
            if s == sum_ - x:
                max_ = max(max_, R - L + 1)
        return len(nums) - max_ if max_ != -1 else -1
