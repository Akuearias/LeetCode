from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        earns, losses = [], []
        for transcation in transactions:
            if transcation[0] <= transcation[1]:
                earns.append(transcation)
            else:
                losses.append(transcation)

        earns.sort(key=lambda x: x[0], reverse=True)
        losses.sort(key=lambda x: x[1])

        new_transactions = losses + earns
        S = 0
        for i in range(len(new_transactions)):
            S -= new_transactions[i][0]
            if i != len(new_transactions) - 1:
                S += new_transactions[i][1]

        return -S if S < 0 else 0

solution = Solution()
print(solution.minimumMoney([[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]))