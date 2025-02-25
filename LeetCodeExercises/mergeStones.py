from typing import List


class Solution:
    def buildCostListHelper(self, cost_list, stones, k, cost=0):
        stones_dup = stones.copy()
        L = len(stones)
        for i in range(0, L - k + 1):
            if len(stones_dup) == 1:
                stones_dup = stones
                cost = 0
            self.buildCostList(cost_list, stones_dup, k, cost)

    def buildCostList(self, cost_list, stones, k, cost=0):
        if len(stones) > 1:
            cost += sum(stones[len(stones):len(stones) + k])
            stones[len(stones):len(stones) + k] = [cost]
            self.buildCostList(cost_list, stones, k, cost)
        else:
            cost_list.append(cost)

    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones) - 1) % (k - 1) != 0:
            return -1
        else:
            cost_list = []
            self.buildCostListHelper(cost_list, stones, k, 0)
            return min(cost_list)


solution = Solution()
print(solution.mergeStones([6, 4, 4, 6], k=2))


