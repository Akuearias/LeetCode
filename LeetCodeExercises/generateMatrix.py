from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        fill_list = [i + 1 for i in range(n*n)]
        r, c = 0, 0
        for num in fill_list:
            matrix[r][c] = num
            if (r - 1 < 0 or matrix[r - 1][c] != 0) and c + 1 < n and matrix[r][c + 1] == 0:
                c += 1
            elif (c + 1 >= n or matrix[r][c + 1] != 0) and r + 1 < n and matrix[r + 1][c] == 0:
                r += 1
            elif (r + 1 >= n or matrix[r + 1][c] != 0) and c - 1 >= 0 and matrix[r][c - 1] == 0:
                c -= 1
            elif (c - 1 < 0 or matrix[r][c - 1] != 0) and r - 1 >= 0 and matrix[r - 1][c] == 0:
                r -= 1
        return matrix


solution = Solution()
print(solution.generateMatrix(2))
