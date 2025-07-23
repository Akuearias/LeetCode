from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        S = []
        i = 0
        j = 0
        m, n = len(matrix), len(matrix[0])
        a, w, s, d = 0, 0, m - 1, n - 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dummy = directions[0]
        for _ in range(m*n):

            S.append(matrix[i][j])
            if i == w and j < d and dummy == directions[0]:
                j += 1
                if j == d and dummy == directions[0]:
                    w += 1
                    dummy = directions[1]
            elif j == d and i < s and dummy == directions[1]:
                i += 1
                if i == s and dummy == directions[1]:
                    d -= 1
                    dummy = directions[2]
            elif i == s and j > a and dummy == directions[2]:
                j -= 1
                if j == a and dummy == directions[2]:
                    s -= 1
                    dummy = directions[3]
            elif j == a and i > w and dummy == directions[3]:
                i -= 1
                if i == w and dummy == directions[3]:
                    a += 1
                    dummy = directions[0]


        return S


if __name__ == '__main__':
    solution = Solution()
    assert solution.spiralOrder([[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]]) == [1,2,3,4,5,6,7,8,9,10,20,19,18,17,16,15,14,13,12,11]
