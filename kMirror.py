class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def Palindrome(x: int) -> bool:
            D = list()
            while x:
                D.append(x % k)
                x //= k
            return D == D[::-1]

        L, count, S = 1, 0, 0
        while count < n:
            R = L * 10
            for even in [0, 1]:
                for i in range(L, R):
                    if count == n:
                        break

                    dummy = i
                    x = (i // 10 if even == 0 else i)
                    while x:
                        dummy = dummy * 10 + x % 10
                        x //= 10
                    if Palindrome(dummy):
                        count += 1
                        S += dummy
            L = R
        return S

# https://leetcode.cn/problems/sum-of-k-mirror-numbers/solutions/1115277/k-jing-xiang-shu-zi-de-he-by-leetcode-so-nyos