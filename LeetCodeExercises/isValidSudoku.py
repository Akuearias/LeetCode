from typing import List

'''



'''

class Solution:
    def rowValid(self, row: List[str]) -> bool:
        elements = []
        for i in row:
            if i.isnumeric():
                elements.append(i)
        return len(set(elements)) == len(elements)

    def columnValid(self, column: List[str]) -> bool:
        elements = []
        for i in column:
            if i.isnumeric():
                elements.append(i)
        return len(set(elements)) == len(elements)

    def matrixValid(self, matrix: List[List[str]]) -> bool:
        elements = []
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j.isnumeric():
                    elements.append(j)
        return len(set(elements)) == len(elements)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        B = True
        for row in board:
            B = B and self.rowValid(row)

        for i in range(0, 9):
            column = []
            for row in board:
                column.append(row[i])
            B = B and self.columnValid(column)

        matrix = []
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                matrix.append(board[i][j:j+3])
                matrix.append(board[i+1][j:j+3])
                matrix.append(board[i+2][j:j+3])
                B = B and self.matrixValid(matrix)
                matrix.clear()

        return B


if __name__ == "__main__":
    board =[["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution = Solution()
    print(solution.isValidSudoku(board))
