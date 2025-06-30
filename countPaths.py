from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def DFS(i, j):
            dummy = 1
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    dummy += DFS(x, y)

            return dummy % (10 ** 9 + 7)

        S = sum(DFS(i, j) for i in range(m) for j in range(n)) % (10 ** 9 + 7)
        return S

# https://leetcode.cn/problems/number-of-increasing-paths-in-a-grid/solutions/1641515/ji-yi-hua-sou-suo-pythonjavacgo-by-endle-xecc