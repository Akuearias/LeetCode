from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        r = len(obstacleGrid) - 1
        c = len(obstacleGrid[0]) - 1

        if obstacleGrid[r][c] == 1 or obstacleGrid[0][0] == 1:
            return 0

        for row in range(len(paths)):
            if obstacleGrid[row][0] == 0:
                if row - 1 < 0:
                    paths[row][0] = 1
                if paths[row - 1][0] != 0:
                    paths[row][0] = 1
        i = 0
        while i <= r:
            for j in range(1, c + 1):
                if obstacleGrid[i][j] == 0:
                    if i - 1 >= 0 and obstacleGrid[i - 1][j] == 0 and paths[i - 1][j] != 0:
                        paths[i][j] += paths[i - 1][j]
                    if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0 and paths[i][j - 1] != 0:
                        paths[i][j] += paths[i][j - 1]
            i += 1

        return paths[r][c]


solution = Solution()
print(solution.uniquePathsWithObstacles([[0,0], [1,1], [0,0]]))
