'''

LeetCode Exercise #57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0

        # 1. Empty: direct insert
        if n == 0:
            return [newInterval]

        # 2. Find the left part to insert
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        # 3. Find overlaps and merge-insert
        while i < n:
            if newInterval[0] <= intervals[i][1]:
                new_start = min(newInterval[0], intervals[i][0])

                j = i
                while j < n and newInterval[1] >= intervals[j][0]:
                    j += 1

                new_end = max(newInterval[1], intervals[j - 1][1])

                return intervals[:i] + [[new_start, new_end]] + intervals[j:]

            i += 1

        # 4. If no returns from the while-loop, it means that it should be inserted in the end
        if newInterval[0] <= intervals[-1][1]:
            intervals[-1][1] = max(intervals[-1][1], newInterval[1])
        else:
            intervals.append(newInterval)

        return intervals


if __name__ == '__main__':
    solution = Solution()
    # assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    # assert solution.insert([[1, 5]], [5, 7]) == [[1, 7]]
    assert solution.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]