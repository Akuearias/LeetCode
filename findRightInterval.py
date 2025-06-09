from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            if intervals[0][0] < intervals[0][1]:
                return [-1]
            else:
                return [0]

        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        n = len(intervals)
        S = [-1] * n
        for _, E, id in intervals:
            i = bisect_left(intervals, [E])
            if i < n:
                S[id] = intervals[i][2]
        return S
