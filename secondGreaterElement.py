from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        L, R = 0, nums[-1] - nums[0]
        while L < R:
            m = (L + R) // 2
            dummy, i = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= m:
                    dummy += 1
                    i += 2
                else:
                    i += 1

            if dummy >= p:
                R = m
            else:
                L = m + 1

        return L

# https://leetcode.cn/problems/next-greater-element-iv/solutions/2562064/xia-yi-ge-geng-da-yuan-su-iv-by-leetcode-hjqv
