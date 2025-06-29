from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        coords = set()
        for pos in positions:
            coords.add(pos[0])
            coords.add(pos[0] + pos[1])

        coords_sort = sorted(coords)
        id_ = {x: i for i, x in enumerate(coords_sort)}

        n = len(coords_sort)
        H = [0] * n
        heights = []
        curr = 0
        for pos in positions:
            L, R = id_[pos[0]], id_[pos[0] + pos[1]]
            h = max(H[L:R]) + pos[1]
            for i in range(L, R):
                H[i] = h
            curr = max(curr, h)
            heights.append(curr)

        return heights
