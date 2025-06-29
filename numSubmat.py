from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = [[0] * len(mat[0]) for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if j == 0:
                        rows[i][j] = 1
                    else:
                        rows[i][j] = rows[i][j - 1] + 1

        S = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue

                dummy = rows[i][j]
                for k in range(i, -1, -1):
                    if rows[k][j] == 0:
                        break
                    dummy = min(dummy, rows[k][j])
                    S += dummy

        return S

# https://leetcode.cn/problems/count-submatrices-with-all-ones/solutions/336410/tong-ji-quan-1-zi-ju-xing-by-leetcode-solution
