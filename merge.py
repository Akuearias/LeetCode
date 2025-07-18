'''

LeetCode Exercise #56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l : l[0])
        new_intervals = [intervals[0]]
        i = 1
        while i < len(intervals):
            if new_intervals[-1][1] >= intervals[i][0]:
                new_intervals[-1][1] = max(intervals[i][1], new_intervals[-1][1])
            else:
                new_intervals.append(intervals[i])
            i += 1

        return new_intervals


if __name__ == '__main__':
    solution = Solution()
    assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert solution.merge([[1,4],[4,5]]) == [[1,5]]


