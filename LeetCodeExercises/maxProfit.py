from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dummy = dp[i - 1]
            dp[i] = dummy + max(0, prices[i] - prices[i-1])
        return dp[-1]


sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))
