from functools import cache


def adjacent(x, y):
    return abs(ord(x) - ord(y)) == 1 or abs(ord(x) - ord(y)) == 25


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)

        @cache
        def empty(i, j):
            if i > j:
                return True

            if adjacent(s[i], s[j]) and empty(i + 1, j - 1):
                return True

            for k in range(i + 1, j - 1, 2):
                if empty(i, k) and empty(k + 1, j):
                    return True
            return False

        @cache
        def DFS(i):
            if i == n:
                return ""

            dummy = s[i] + DFS(i + 1)
            for j in range(i + 1, n, 2):
                if empty(i, j):
                    dummy = min(dummy, DFS(j + 1))

            return dummy

        return DFS(0)

# https://leetcode.cn/problems/lexicographically-smallest-string-after-adjacent-removals/solutions/3685460/zi-fu-xiao-xiao-le-qu-jian-dp-xian-xing-xmaqk


