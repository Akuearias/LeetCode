import math
from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def Prime_sieve(x):
            prime = [False, False] + [True] * (x - 1)
            for i in range(2, int(math.sqrt(x)) + 1):
                if prime[i]:
                    for j in range(i * i, x + 1, i):
                        prime[j] = False
            return prime

        S = []
        primes = Prime_sieve(n)

        p = 2
        while p <= n // 2:
            if primes[p] is True and primes[n - p] is True:
                S.append([p, n - p])
            p += 1
        return S