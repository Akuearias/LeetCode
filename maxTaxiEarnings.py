from bisect import bisect_right
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda l: l[1])
        DP = [0] * (len(rides) + 1)
        for i in range(len(rides)):
            dummy = bisect_right(rides, rides[i][0], hi=i, key=lambda l: l[1])
            DP[i + 1] = max(DP[i], DP[dummy] + rides[i][1] - rides[i][0] + rides[i][2])

        return DP[-1]
