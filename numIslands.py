from typing import List


# https://leetcode.cn/problems/number-of-islands/solutions/13103/dao-yu-shu-liang-by-leetcode
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(grid, r, c):
            grid[r][c] = 0
            m, n = len(grid), len(grid[0])
            for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    DFS(grid, i, j)

        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])

        S = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    S += 1
                    DFS(grid, i, j)

        return S