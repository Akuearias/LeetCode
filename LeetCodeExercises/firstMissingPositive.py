from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = 1
        for i in range(1, len(nums) + 1):
            if not nums_dict.get(i):
                return i
        return len(nums) + 1


solution = Solution()
assert solution.firstMissingPositive([1, 2, 0]) == 3
