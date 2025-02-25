from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        triangle = []
        triangle.append([1])
        triangle.append([1, 1])

        if numRows == 2:
            return triangle

        for i in range(3, numRows+1):
            row = [1] * (i)
            triangle.append(row)

        m = 2
        while m < numRows:
            n = 1
            while n <= m - 1:
                triangle[m][n] = triangle[m - 1][n - 1] + triangle[m - 1][n]
                n += 1
            m += 1

        return triangle


solution = Solution()
print(solution.generate(5))
