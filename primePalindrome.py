import math


class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(N):
            if N == 1:
                return False

            for i in range(2, int(math.sqrt(N)) + 1):
                if N % i == 0:
                    return False
            return True

        if 8 <= n <= 11:
            return 11

        if 5 < n < 8:
            return 7

        if 3 < n <= 5:
            return 5

        if 1 < n <= 3:
            return n

        for i in range(1, 6):
            for rt in range(10 ** (i - 1), 10 ** i):
                rt_str = str(rt)
                num = int(rt_str + rt_str[-2::-1])
                if num >= n and isPrime(num):
                    return num

        return -1