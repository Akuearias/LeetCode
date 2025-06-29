from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        days = len(pizzas) // 4
        S = 0
        i = 0
        j = 0
        if days % 2 != 0:
            odds = days // 2 + 1
        else:
            odds = days // 2
        evens = days // 2
        while i < odds:
            S += pizzas.pop()
            i += 1
        while j < evens:
            pizzas.pop()
            S += pizzas.pop()
            j += 1

        return S
