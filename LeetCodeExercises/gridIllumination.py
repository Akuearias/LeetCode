from typing import List


class Solution:
    def On(self, lamp, grid):
        n = len(grid)
        row = lamp[0]
        column = lamp[1]
        for i in range(0, n):
            grid[i][column] = 1
            grid[row][i] = 1
        for j in range(0, n):
            if column - j >= 0:
                if row - j >= 0:
                    grid[row - j][column - j] = 1
                if row + j < n:
                    grid[row + j][column - j] = 1
            if column + j < n:
                if row - j >= 0:
                    grid[row - j][column + j] = 1
                if row + j < n:
                    grid[row + j][column + j] = 1

    def Off(self, lamp, grid):
        n = len(grid)
        row = lamp[0]
        column = lamp[1]
        for i in range(0, n):
            grid[i][column] = 0
            grid[row][i] = 0
        for j in range(0, n):
            if column - j >= 0:
                if row - j >= 0:
                    grid[row - j][column - j] = 0
                if row + j < n:
                    grid[row + j][column - j] = 0
            if column + j < n:
                if row - j >= 0:
                    grid[row - j][column + j] = 0
                if row + j < n:
                    grid[row + j][column + j] = 0

    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        grid = [[0 for _ in range(0, n)] for _ in range(0, n)]

        for lamp in lamps:
            self.On(lamp, grid)

        results = []
        for lamp in queries:
            r = lamp[0]
            c = lamp[1]
            if grid[r][c] == 1:
                results.append(1)
            else:
                results.append(0)

            checkList = [[r, c]]
            if r - 1 >= 0:
                checkList.append([r - 1, c])
                if c - 1 >= 0:
                    checkList.append([r - 1, c - 1])
                if c + 1 < n:
                    checkList.append([r - 1, c + 1])

            if r + 1 < n:
                checkList.append([r + 1, c])
                if c - 1 >= 0:
                    checkList.append([r + 1, c - 1])
                if c + 1 < n:
                    checkList.append([r + 1, c + 1])

            if c - 1 >= 0:
                checkList.append([r, c - 1])
                if r - 1 >= 0:
                    checkList.append([r - 1, c - 1])
                if r + 1 < n:
                    checkList.append([r + 1, c - 1])

            if c + 1 < n:
                checkList.append([r, c + 1])
                if r - 1 >= 0:
                    checkList.append([r - 1, c + 1])
                if r + 1 < n:
                    checkList.append([r + 1, c + 1])

            for lamp in checkList:
                grid[lamp[0]][lamp[1]] = 0
                if lamps.__contains__(lamp):
                    self.Off(lamp, grid)
                while lamps.__contains__(lamp):
                    lamps.remove(lamp)

                for l in lamps:
                    self.On(l, grid)

        return results


solution = Solution()
print(solution.gridIllumination(n=6, lamps=[[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]],
                                queries=[[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]))
