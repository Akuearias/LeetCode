from typing import List


# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/537731/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        S1 = [[0 for _ in range(k + 1)] for _ in range(n)]  # Buy
        S2 = [[0 for _ in range(k + 1)] for _ in range(n)]  # Sell

        S1[0][0], S2[0][0] = -prices[0], 0

        for i in range(1, n):
            S1[i][0] = max(S1[i - 1][0], S2[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                S1[i][j] = max(S1[i - 1][j], S2[i - 1][j] - prices[i])
                S2[i][j] = max(S2[i - 1][j], S1[i - 1][j - 1] + prices[i])

        return max(S2[n - 1])