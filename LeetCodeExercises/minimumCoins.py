from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        def dp(S, prices, i):
            if i == 1:
                S += prices[i-1]

            while i < len(prices) - 1:
                for j in range(i+1, i+i):
                    S += min(dp(S, prices, j-1), prices[j])
                i += 1

            return S

        return dp(0, prices, 1)

solution = Solution()
print(solution.minimumCoins([3,1,2]))
