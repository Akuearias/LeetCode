import math
import heapq
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        S = -math.inf
        pq = []
        heapq.heapify(pq)
        for point in points:
            while pq and point[0] - pq[0][1] > k:
                heapq.heappop(pq)

            if pq:
                S = max(S, point[0] + point[1] - pq[0][0])

            heapq.heappush(pq, [point[0] - point[1], point[0]])

        return S

    # https://leetcode.cn/problems/max-value-of-equation/solutions/2351324/man-zu-bu-deng-shi-de-zui-da-zhi-by-leet-5rbj
