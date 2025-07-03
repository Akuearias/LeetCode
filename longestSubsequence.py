import collections
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        DP = [1] * n
        visited = collections.defaultdict(int)
        visited[arr[0]] = 0
        for i in range(1, n):
            if arr[i] - difference in visited:
                DP[i] = DP[visited[arr[i] - difference]] + 1
            visited[arr[i]] = i

        return max(DP)
