from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 3:
            return 0

        if len(nums) == 3:
            return 1 if nums[0] + nums[1] > nums[2] else 0

        third = len(nums) - 1
        S = 0
        while third > 1:
            first, second = 0, third - 1
            while first < second:
                if nums[first] + nums[second] > nums[third]:
                    S += second - first
                    second -= 1
                else:
                    first += 1
            third -= 1

        return S


