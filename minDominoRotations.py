'''

LeetCode Exercise #1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.



Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Constraints:

2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6

'''
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_list, bottom_list = [0] * 7, [0] * 7
        totals = [0] * 7
        duplicates = [0] * 7

        N = len(tops)

        for i in range(N):
            dup = 0
            top_list[tops[i]] += 1
            bottom_list[bottoms[i]] += 1
            totals[tops[i]] += 1
            if tops[i] != bottoms[i]:
                totals[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                dup += 1
            duplicates[tops[i]] += dup

        for i in range(1, 7):
            if totals[i] >= N:
                return min(top_list[i], bottom_list[i]) - duplicates[i]

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.minDominoRotations(tops=[2,1,2,4,2,2], bottoms=[5,2,6,2,3,2]) == 2
    assert solution.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]) == -1
    assert solution.minDominoRotations([1,3,4,1,2,1,3,4], [1,3,1,2,2,1,4,4]) == -1
    assert solution.minDominoRotations([1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]) == 0
