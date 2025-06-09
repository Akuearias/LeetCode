from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        diff, total = nums[1] - nums[0], 0
        S = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                total += 1

            else:
                diff = nums[i] - nums[i - 1]
                total = 0

            S += total

        return S
