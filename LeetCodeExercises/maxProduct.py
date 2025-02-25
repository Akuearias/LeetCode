import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(2, len(nums)+1):
            for j in range(1, i):
                dummy = dp[j-1]
                dp[j] = max(dummy, nums[j] * nums[j-1])
        return max(dp)


solution = Solution()
print(solution.maxProduct([2,3,-2,4]))
print(solution.maxProduct([-2,0,-1]))
print(solution.maxProduct([-3,-1,-1]))
