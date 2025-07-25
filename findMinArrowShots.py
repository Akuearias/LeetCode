from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda l: l[1])
        S = 1
        curr = points[0][1]

        for balloon in points[1:]:
            if balloon[0] > curr:
                S += 1
                curr = balloon[1]

        return S