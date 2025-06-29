from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        map_ = [[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    map_[i][j] = 0

        dq = deque((i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water)
        while dq:
            i, j = dq.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                 if 0 <= x < len(isWater) and 0 <= y < len(isWater[0]) and map_[x][y] == -1:
                    map_[x][y] = map_[i][j] + 1
                    dq.append((x, y))

        return map_

# https://leetcode.cn/problems/map-of-highest-peak/solutions/1234660/di-tu-zhong-de-zui-gao-dian-by-leetcode-jdkzr
