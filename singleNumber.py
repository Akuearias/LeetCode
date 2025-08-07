from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        S = 0
        for num in nums:
            S = S ^ num

        return S