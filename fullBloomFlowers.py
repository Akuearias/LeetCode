from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]

'''

https://leetcode.cn/problems/number-of-flowers-in-full-bloom/solutions/2457828/hua-qi-nei-hua-de-shu-mu-by-leetcode-sol-j94l/

'''