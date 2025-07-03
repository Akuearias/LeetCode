class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base = 131
        L, R = 0, 0
        m = 1
        S = -1

        for i in range(n):
            L = (L * base + ord(s[i])) % (10 ** 9 + 7)
            R = (R + m * ord(s[i])) % (10 ** 9 + 7)
            if L == R:
                S = i

            m = m * base % (10 ** 9 + 7)

        s2 = ("" if S == n - 1 else s[S + 1:])
        return s2[::-1] + s

# https://leetcode.cn/problems/shortest-palindrome/solutions/392561/zui-duan-hui-wen-chuan-by-leetcode-solution
