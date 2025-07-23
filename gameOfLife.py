from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        alive = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                surround = []
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        surround.append((i - 1, j - 1))
                    surround.append((i - 1, j))
                    if j + 1 < n:
                        surround.append((i - 1, j + 1))

                if i + 1 < m:
                    if j - 1 >= 0:
                        surround.append((i + 1, j - 1))
                    surround.append((i + 1, j))
                    if j + 1 < n:
                        surround.append((i + 1, j + 1))

                if j - 1 >= 0:
                    surround.append((i, j - 1))

                if j + 1 < n:
                    surround.append((i, j + 1))

                dummy = 0
                for s in surround:
                    if board[s[0]][s[1]] == 1:
                        dummy += 1

                if board[i][j] == 1:
                    if dummy == 2 or dummy == 3:
                        alive[i][j] = True

                else:
                    if dummy == 3:
                        alive[i][j] = True

        for i in range(m):
            for j in range(n):
                if alive[i][j] == True:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
