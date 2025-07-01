import heapq
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        pq = []
        heapq.heapify(pq)
        S = 0
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            j = 0
            while j < limits[i]:
                heapq.heappush(pq, -1 * grid[i][j])
                j += 1

        for _ in range(k):
            S += -1 * heapq.heappop(pq)
        return S

if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSum([[1, 2], [3, 4]], [1, 2], 2) == 7