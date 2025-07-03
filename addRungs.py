from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        stairs = [0] + rungs
        S = 0
        for i in range(1, len(stairs)):
            prev = stairs[i - 1]
            next_ = stairs[i]
            if next_ - prev > dist:
                if (next_ - prev) % dist != 0:
                    S += (next_ - prev) // dist
                else:
                    S += (next_ - prev) // dist - 1

        return S
