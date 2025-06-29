from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        DP = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    DP[i] += DP[i - num]

        return DP[-1]

# https://leetcode.cn/problems/combination-sum-iv/solutions/740581/zu-he-zong-he-iv-by-leetcode-solution-q8zv