from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def valid(target, i, nums):
            for n in range(len(nums)):
                if i + nums[n] >= target:
                    return True
            return False

        if len(nums) == 1:
            return True

        if len(nums) > 1 and nums[0] == 0:
            return False

        B = True
        target = nums[-1]
        while i < len(nums) - 1:
            if valid(target, i, nums):
                i = 0
                target = 
            else:




solution = Solution()
assert solution.canJump([1,0,1,0]) == False
