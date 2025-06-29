import math
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        S = len(nums)

        mono_stack = [[math.inf, 0]]
        for i in range(len(nums)):
            while nums[i] > mono_stack[-1][0]:
                mono_stack.pop()

            if nums[i] == mono_stack[-1][0]:
                S += mono_stack[-1][1]
                mono_stack[-1][1] += 1

            else:
                mono_stack.append([nums[i], 1])

        return S

# https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/solutions/2738894/on-dan-diao-zhan-pythonjavacgo-by-endles-y00d