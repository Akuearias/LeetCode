from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        res = float('inf')

        def dfs(u):
            nonlocal res
            visited.add(u)
            for v, w in graph[u]:
                res = min(res, w)
                if v not in visited:
                    dfs(v)

        dfs(1)
        return res