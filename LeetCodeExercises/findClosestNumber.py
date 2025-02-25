import math
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0

        to_zero = math.inf
        val = None
        for i in range(len(nums)):
            dummy = to_zero
            to_zero = min(to_zero, abs(nums[i]))
            if not val:
                val = nums[i]
            if dummy == to_zero and val < nums[i] and abs(val) == abs(nums[i]):
                val = nums[i]
            elif dummy > to_zero:
                val = nums[i]


        return val


solution = Solution()
assert solution.findClosestNumber([-1, 0, 2, 3, 4, 5]) == 0
