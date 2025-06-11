from typing import List
import numpy as np


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid_v = [list(row) for row in np.array(grid).T]

        skyline_W, skyline_S = [], []

        for i in range(len(grid_v)):
            skyline_S.append(max(grid_v[i]))

        for i in range(len(grid)):
            skyline_W.append(max(grid[i]))

        S = 0
        for i in range(m):
            for j in range(n):
                dummy = grid[i][j]
                new_ = min(skyline_S[j], skyline_W[i])
                grid[i][j] = new_
                S += new_ - dummy

        return int(S)


