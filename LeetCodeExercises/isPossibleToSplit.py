from typing import List
from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums_dict = dict(Counter(nums))
        for num in list(nums_dict.values()):
            if num > 2:
                return False
        return True
