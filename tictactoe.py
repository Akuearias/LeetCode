from typing import List


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        def rowWin(board, pattern):
            B = False
            for i in range(len(board)):
                b = (board[i][0] == pattern)
                for j in range(1, len(board)):
                    b &= (board[i][j] == pattern)
                B |= b

            return B

        def colWin(board, pattern):
            B = False
            for i in range(len(board)):
                b = (board[0][i] == pattern)
                for j in range(1, len(board)):
                    b &= (board[j][i] == pattern)
                B |= b

            return B

        def diagWin(board, pattern):
            B1, B2 = (board[0][0] == pattern), (board[0][len(board) - 1] == pattern)
            for i in range(1, len(board)):
                B1 &= (board[i][i] == pattern)
                B2 &= (board[i][len(board) - 1 - i] == pattern)

            return B1 or B2

        if len(board) == 1:
            return board[0][0] if board[0][0] != " " else "Pending"

        n = len(board)

        if rowWin(board, 'O') or colWin(board, 'O') or diagWin(board, 'O'):
            return 'O'

        if rowWin(board, 'X') or colWin(board, 'X') or diagWin(board, 'X'):
            return 'X'

        S = 0
        for i in range(len(board)):
            for char in board[i]:
                if char != ' ':
                    S += 1

        if S != n * n:
            return "Pending"
        else:
            return "Draw"
