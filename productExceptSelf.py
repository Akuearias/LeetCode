from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_production = [1] * n
        suffix_production = [1] * n
        S = [1] * n
        for i in range(1, n):
            prefix_production[i] = prefix_production[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix_production[i] = suffix_production[i + 1] * nums[i + 1]

        for i in range(n):
            S[i] = prefix_production[i] * suffix_production[i]

        return S
