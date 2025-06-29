from typing import List


class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        DP = [0] * (k + 1)
        DP[0] = 1

        for _, cap in enumerate(capacities):
            cap -= 1
            for j in range(k, cap - 1, -1):
                DP[j] = (DP[j] + DP[j - cap]) % (10**9 + 7)

        return DP[-1]

# https://leetcode.cn/problems/oPs9Bm/solutions/1016968/zhuan-huan-wei-01-bei-bao-fang-an-shu-by-1dax