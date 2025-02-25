from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums = nums[-1::-1]

        tail = nums[-1]

