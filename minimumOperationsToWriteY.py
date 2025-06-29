import collections
from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        S = 0
        Ys = set()
        n = len(grid)
        for i in range((n - 1) // 2 + 1):
            Ys.add((i, i))
            Ys.add((i, n - 1 - i))

        for i in range((n - 1) // 2 + 1, n):
            Ys.add((i, (n - 1) // 2))

        Y_components = collections.defaultdict(int)
        non_Y_components = collections.defaultdict(int)

        for (x, y) in Ys:
            Y_components[grid[x][y]] += 1

        for i in range(n):
            for j in range(n):
                if (i, j) not in Ys:
                    non_Y_components[grid[i][j]] += 1

        total_counts = []
        total_counts.append(Y_components[0] + non_Y_components[1])
        total_counts.append(Y_components[0] + non_Y_components[2])
        total_counts.append(Y_components[1] + non_Y_components[0])
        total_counts.append(Y_components[1] + non_Y_components[2])
        total_counts.append(Y_components[2] + non_Y_components[0])
        total_counts.append(Y_components[2] + non_Y_components[1])
        total_counts.sort()

        return n * n - total_counts[-1]
