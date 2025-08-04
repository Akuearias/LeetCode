from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        S = []

        def BT(start, path):
            if len(path) == k:
                S.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                BT(i + 1, path)
                path.pop()

        BT(1, [])
        return S



