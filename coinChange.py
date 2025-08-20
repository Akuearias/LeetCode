from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        S = [0] + [math.inf for _ in range(amount)]
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    S[i + coin] = min(S[i] + 1, S[i + coin])

        if S[-1] != math.inf:
            return S[-1]
        else:
            return -1
