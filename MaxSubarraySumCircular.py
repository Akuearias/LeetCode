from typing import List


# https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/2350660/huan-xing-zi-shu-zu-de-zui-da-he-by-leet-elou
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        L = [0] * n

        L[0], l = nums[0], nums[0]
        p, q = nums[0], nums[0]

        for i in range(1, n):
            p = max(p + nums[i], nums[i])
            q = max(q, p)
            l += nums[i]
            L[i] = max(L[i - 1], l)

        r = 0
        for i in range(n - 1, 0, -1):
            r += nums[i]
            q = max(q, r + L[i - 1])

        return q
