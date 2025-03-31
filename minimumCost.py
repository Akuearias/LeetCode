from typing import List

'''
There is an m x n cake that needs to be cut into 1 x 1 pieces.

You are given integers m, n, and two arrays:

horizontalCut of size m - 1, where horizontalCut[i] represents the cost to cut along the horizontal line i.
verticalCut of size n - 1, where verticalCut[j] represents the cost to cut along the vertical line j.
In one operation, you can choose any piece of cake that is not yet a 1 x 1 square and perform one of the following cuts:

Cut along a horizontal line i at a cost of horizontalCut[i].
Cut along a vertical line j at a cost of verticalCut[j].
After the cut, the piece of cake is divided into two distinct pieces.

The cost of a cut depends only on the initial cost of the line and does not change.

Return the minimum total cost to cut the entire cake into 1 x 1 pieces.
'''

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut = sorted(horizontalCut)
        verticalCut = sorted(verticalCut)
        totalCost = 0
        i = 1
        j = 1
        while horizontalCut or verticalCut:
            if not verticalCut or (horizontalCut and horizontalCut[-1] > verticalCut[-1]):
                totalCost += horizontalCut.pop() * i
                j += 1
            else:
                totalCost += verticalCut.pop() * j
                i += 1
        return totalCost


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumCost(6, 3, [2,3,2,3,1], [1,2]))



