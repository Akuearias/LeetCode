from math import gcd
from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        k = gcd(k, len(arr))
        ans = 0
        for i in range(k):
            b = sorted(arr[i::k])
            mid = b[len(b) // 2]
            ans += sum(abs(x - mid) for x in b)
        return ans

'''
References:
https://leetcode.cn/problems/make-k-subarray-sums-equal/solutions/2203591/zhuan-huan-zhong-wei-shu-tan-xin-pei-shu-4dut/
'''