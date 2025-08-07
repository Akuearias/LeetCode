from typing import List


# https://leetcode.cn/problems/single-number-ii/solutions/746993/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        S = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    S -= (1 << i)
                else:
                    S |= (1 << i)

        return S