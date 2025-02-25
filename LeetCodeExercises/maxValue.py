from typing import List
from itertools import combinations


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 2:
            return nums[0] ^ nums[1]
        n = len(nums)
        L_nums = nums[0:n//2]
        R_nums = nums[n//2:]
        L_or, R_or = [], []
        for comb in combinations(L_nums, k):
            logic_or = comb[0]
            for c in comb[1:]:
                logic_or |= c
            L_or.append(logic_or)

        for comb in combinations(R_nums, k):
            logic_or = comb[0]
            for c in comb[1:]:
                logic_or |= c
            R_or.append(logic_or)


        xors = [l ^ r for l in L_or for r in R_or]
        return max(xors)


solution = Solution()
print(solution.maxValue([1,89,11,90], 2))



