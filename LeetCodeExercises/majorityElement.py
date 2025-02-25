from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = dict(Counter(nums))
        for num in nums:
            if nums_dict[num] > len(nums)/2:
                return num


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
