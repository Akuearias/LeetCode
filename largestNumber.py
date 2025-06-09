from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums.sort(key=lambda l: l[0])
        largest = ""

        for j in range(len(nums) - 1, -1, -1):
            largest += nums[j]

        return largest
