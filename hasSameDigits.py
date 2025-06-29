MX = 5
c = [[0] * MX for i in range(MX)]
for i in range(MX):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]


def lucas(n: int, k: int, p: int) -> int:
    if k == 0:
        return 1
    return c[n % p][k % p] * lucas(n // p, k // p, p) % p


def comb(n: int, k: int) -> int:
    return lucas(n, k, 2) * 5 + lucas(n, k, 5) * 6


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        s = map(ord, s)
        return sum(comb(n - 2, i) * (x - y) for i, (x, y) in enumerate(pairwise(s))) % 10 == 0


'''

https://leetcode.cn/problems/check-if-digits-are-equal-in-string-after-operations-ii/solutions/

'''
