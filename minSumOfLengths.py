import math
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        DP = [math.inf] * (n + 1)
        prefix_sums = [0] * (n + 1)
        L = 0
        length = math.inf
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + arr[i]

        for i in range(n):
            while prefix_sums[i + 1] - prefix_sums[L] > target:
                L += 1
            if prefix_sums[i + 1] - prefix_sums[L] == target:
                length = min(length, DP[L] + i - L + 1)
                DP[i + 1] = min(DP[i], i - L + 1)

            else:
                DP[i + 1] = DP[i]

        return length if length < math.inf else -1
