from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for zero in zeros:
            for i in range(m):
                matrix[i][zero[1]] = 0
            for j in range(n):
                matrix[zero[0]][j] = 0