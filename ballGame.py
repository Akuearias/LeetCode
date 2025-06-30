from typing import List


# This code exceeds the time limit. Though it uses a reverse method, i.e. from holes to edges,
# theoretically quicker than the standard solution, I don't know why it exceeds the time limit.
# Solution: https://leetcode.cn/problems/EXvqDp/solutions/1847059/mei-ju-by-endlesscheng-5wzf
class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        holes = set()
        edges = set()

        S = set()
        m, n = len(plate), len(plate[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1:
                    if 0 < j < n - 1 and plate[i][j] != 'E' and plate[i][j] != 'W':
                        edges.add((i, j))
                elif j == 0 or j == n - 1:
                    if 0 < i < m - 1 and plate[i][j] != 'E' and plate[i][j] != 'W':
                        edges.add((i, j))

                if plate[i][j] == 'O':
                    holes.add((i, j))
                    if (i, j) in edges:
                        edges.remove((i, j))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # D - S - A - W
        for hole in holes:
            for i in range(4):
                k = 0
                start = list(hole)
                curr_dir = i

                while k <= num:
                    if plate[start[0]][start[1]] == 'E':
                        curr_dir = (curr_dir + 3) % 4
                    elif plate[start[0]][start[1]] == 'W':
                        curr_dir = (curr_dir + 1) % 4

                    if (start[0], start[1]) in edges:
                        if ((start[0] == 0 and curr_dir == 1)
                        or (start[0] == m - 1 and curr_dir == 3)
                        or (start[1] == 0 and curr_dir == 0)
                        or (start[1] == n - 1 and curr_dir == 2)):
                            S.add((start[0], start[1]))
                            break

                    nx = start[0] - dirs[curr_dir][0]
                    ny = start[1] - dirs[curr_dir][1]

                    if not (0 <= nx < m and 0 <= ny < n):
                        break

                    start[0], start[1] = nx, ny
                    k += 1

        return [list(s) for s in sorted(S)]