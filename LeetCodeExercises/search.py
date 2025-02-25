from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        L = 0
        R = len(nums) - 1
        while L <= R:
            i = (L + R) // 2
            if nums[i] > target:
                R = i - 1
            elif nums[i] < target:
                L = i + 1
            elif nums[i] == target:
                return True
        return False


