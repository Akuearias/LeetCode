from typing import List


class Solution:
    def return2Dcoordinate(self, mat, i):
        for r in mat:
            if r.__contains__(i):
                for c in r:
                    if c == i:
                        return mat.index(r), r.index(c)

        return -1, -1

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rookCoor = self.return2Dcoordinate(board, 'R')
        columns = []
        rows = []
        for c in board[rookCoor[0]]:
            if c != '.':
                columns.append(c)
        for r in board:
            if r[rookCoor[1]] != '.':
                rows.append(r[rookCoor[1]])

        S = 0
        if len(rows) > 1 and rows.index('R') + 1 < len(rows) and rows[rows.index('R') + 1] == 'p':
            S += 1
        if len(rows) > 1 and rows.index('R') - 1 >= 0 and rows[rows.index('R') - 1] == 'p':
            S += 1
        if len(columns) > 1 and columns.index('R') + 1 < len(columns) and columns[columns.index('R') + 1] == 'p':
            S += 1
        if len(columns) > 1 and columns.index('R') - 1 >= 0 and columns[columns.index('R') - 1] == 'p':
            S += 1

        return S


solution = Solution()
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(solution.numRookCaptures(board))




