from typing import List

'''

LeetCode Exercise #36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

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
