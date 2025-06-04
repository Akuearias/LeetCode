from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            L, R = 0, len(matrix[i]) - 1
            while L <= R:
                mid = (L + R) // 2
                if matrix[i][mid] > target:
                    R = mid - 1
                elif matrix[i][mid] < target:
                    L = mid + 1
                else:
                    return True

        return False