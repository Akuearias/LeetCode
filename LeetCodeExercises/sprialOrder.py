from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        flag = "→"
        r = 0
        if flag == "→":
            for i in range(len(matrix[0])):
                order.append(matrix[0][i])