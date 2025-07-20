from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def DFS(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            B = False
            for dir_ in dirs:
                dummyi, dummyj = i + dir_[0], j + dir_[1]
                if 0 <= dummyi < len(board) and 0 <= dummyj < len(board[0]):
                    if (dummyi, dummyj) not in visited:
                        if DFS(dummyi, dummyj, k + 1):
                            B = True
                            break

            visited.remove((i, j))
            return B

        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if DFS(i, j, 0):
                    return True

        return False


