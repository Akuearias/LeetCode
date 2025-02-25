from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        L = 0
        R = sum(nums)
        S = 0
        for i in range(0, len(nums) - 1):
            L += nums[i]
            R -= nums[i]
            if L >= R:
                S += 1

        return S

solution = Solution()
print(solution.waysToSplitArray([2,3,1,0]))