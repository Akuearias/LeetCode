from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def count2(num):
            S = 0
            while num % 2 == 0:
                S += 1
                num //= 2
            return S

        def count5(num):
            S = 0
            while num % 5 == 0:
                S += 1
                num //= 5
            return S

        L2, L5, R2, R5, U2, U5, D2, D5 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)], [[0] * n for _ in
                                                                                                    range(m)], [[0] * n
                                                                                                                for _ in
                                                                                                                range(
                                                                                                                    m)], [
            [0] * n for _ in range(m)], [[0] * n for _ in range(m)], [[0] * n for _ in range(m)], [[0] * n for _ in
                                                                                                   range(m)]

        for i in range(m):
            for j in range(n):
                if i:
                    U2[i][j] = U2[i - 1][j] + count2(grid[i - 1][j])
                    U5[i][j] = U5[i - 1][j] + count5(grid[i - 1][j])
                if j:
                    L2[i][j] = L2[i][j - 1] + count2(grid[i][j - 1])
                    L5[i][j] = L5[i][j - 1] + count5(grid[i][j - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i != m - 1:
                    D2[i][j] = D2[i + 1][j] + count2(grid[i + 1][j])
                    D5[i][j] = D5[i + 1][j] + count5(grid[i + 1][j])

                if j != n - 1:
                    R2[i][j] = R2[i][j + 1] + count2(grid[i][j + 1])
                    R5[i][j] = R5[i][j + 1] + count5(grid[i][j + 1])

        S = 0
        for i in range(m):
            for j in range(n):
                C2 = count2(grid[i][j])
                C5 = count5(grid[i][j])
                S = max(S, min(U2[i][j] + L2[i][j] + C2, U5[i][j] + L5[i][j] + C5))
                S = max(S, min(U2[i][j] + R2[i][j] + C2, U5[i][j] + R5[i][j] + C5))
                S = max(S, min(D2[i][j] + L2[i][j] + C2, D5[i][j] + L5[i][j] + C5))
                S = max(S, min(D2[i][j] + R2[i][j] + C2, D5[i][j] + R5[i][j] + C5))

        return S