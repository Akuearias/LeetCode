import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_counts = dict(collections.Counter(nums))
        for num in nums_counts.keys():
            if nums_counts[num] == 1:
                return -1

        S = 0
        nums_counts_values = list(nums_counts.values())
        for num in nums_counts_values:
            if num % 3 == 0:
                S += num // 3
            elif num % 3 == 2:
                S += num // 3 + 1
            else:
                S += num // 3 - 1 + 2

        return S
