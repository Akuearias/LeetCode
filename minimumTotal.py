from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        DP = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
        DP[0][0] = triangle[0][0]

        for i in range(1, len(DP)):
            for j in range(i + 1):
                if j == 0:
                    DP[i][j] = DP[i - 1][j] + triangle[i][j]
                else:
                    D1 = DP[i - 1][j - 1] + triangle[i][j]
                    if j <= i - 1:
                        D2 = DP[i - 1][j] + triangle[i][j]
                    else:
                        D2 = math.inf
                    DP[i][j] = min(D1, D2)

        return min(DP[-1])


