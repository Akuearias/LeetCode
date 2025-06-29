from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = 0
        res = 0
        for t in transactions:
            cost, cashback = t[0], t[1]
            total_lose += max(cost - cashback, 0)
            res = max(res, min(cost, cashback))
        return total_lose + res

# https://leetcode.cn/problems/minimum-money-required-before-transactions/solutions/3047584/wan-cheng-suo-you-jiao-yi-de-chu-shi-zui-cde1

solution = Solution()
print(solution.minimumMoney([[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]))