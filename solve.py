# https://leetcode.cn/problems/surrounded-regions/solutions/369110/bei-wei-rao-de-qu-yu-by-leetcode-solution
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def DFS(x, y):
            if not 0 <= x < len(board) or not 0 <= y < len(board[0]) or board[x][y] != 'O':
                return

            board[x][y] = 'A'
            DFS(x + 1, y)
            DFS(x - 1, y)
            DFS(x, y + 1)
            DFS(x, y - 1)

        if not board:
            return

        m, n = len(board), len(board[0])

        for i in range(m):
            DFS(i, 0)
            DFS(i, n - 1)

        for i in range(n):
            DFS(0, i)
            DFS(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'