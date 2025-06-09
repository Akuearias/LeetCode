from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix_list = matrix[0]
        for i in range(1, len(matrix)):
            matrix_list += matrix[i]

        matrix_list.sort()
        return matrix_list[k - 1]