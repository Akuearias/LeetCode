from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        dummy = []
        for hour in hours:
            if hour > 8:
                dummy.append(1)
            else:
                dummy.append(-1)

        prefix_sum = [0]
        for d in dummy:
            prefix_sum.append(prefix_sum[-1] + d)

        stack = []
        for i in range(len(prefix_sum)):
            if not stack or prefix_sum[i] < prefix_sum[stack[-1]]:
                stack.append(i)

        S = 0
        for j in range(len(prefix_sum) - 1, -1, -1):
            while stack and prefix_sum[j] > prefix_sum[stack[-1]]:
                S = max(S, j - stack.pop())
        return S