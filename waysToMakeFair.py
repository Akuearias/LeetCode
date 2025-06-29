from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        odd_prefix, even_prefix = [0] * (len(nums) + 1), [0] * (len(nums) + 1)
        for i in range(len(nums)):
            odd_prefix[i + 1] = odd_prefix[i]
            even_prefix[i + 1] = even_prefix[i]
            if i % 2 == 0:
                even_prefix[i + 1] += nums[i]
            else:
                odd_prefix[i + 1] += nums[i]

        S = 0
        for i in range(len(nums)):
            S_even = even_prefix[i] + odd_prefix[-1] - odd_prefix[i + 1]
            S_odd = odd_prefix[i] + even_prefix[-1] - even_prefix[i + 1]
            if S_even == S_odd:
                S += 1
        return S
