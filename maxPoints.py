from typing import List
import math


# https://leetcode.cn/problems/max-points-on-a-line/solutions/842114/zhi-xian-shang-zui-duo-de-dian-shu-by-le-tq8f
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ret = 0
        for i in range(n):
            if ret >= n - i or ret > n // 2:
                break
            slope_count = {}
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    if y < 0:
                        x, y = -x, -y
                    g = math.gcd(abs(x), abs(y))
                    x //= g
                    y //= g
                slope_count[(x, y)] = slope_count.get((x, y), 0) + 1
            maxn = max(slope_count.values(), default=0) + 1
            ret = max(ret, maxn)
        return ret

