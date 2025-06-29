from collections import deque
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        S = -1
        maxProfit = 0
        totalProfit = 0
        oper = 0
        customers_num = 0
        customers = deque(customers)
        while customers:
            oper += 1
            customers_num += customers.popleft()
            curr = min(4, customers_num)
            customers_num -= curr
            totalProfit += boardingCost * curr - runningCost
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                S = oper

        if customers_num == 0:
            return S

        each = boardingCost * 4 - runningCost
        if each <= 0:
            return S

        if customers_num > 0:
            rest = customers_num // 4
            totalProfit += each * rest
            oper += rest
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                S = oper

            remain = customers_num % 4
            remainProfit = boardingCost * remain - runningCost
            totalProfit += remainProfit
            if totalProfit > maxProfit:
                oper += 1
                S += 1

        return S

# https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/solutions/2147029/jing-ying-mo-tian-lun-de-zui-da-li-run-b-4mdh
