import collections
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = collections.defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(o: int, pre: int):
            f[o][ord(labels[o]) - ord("a")] = 1
            for nex in g[o]:
                if nex != pre:
                    dfs(nex, o)
                    for i in range(26):
                        f[o][i] += f[nex][i]

        f = [[0] * 26 for _ in range(n)]
        dfs(0, -1)

        ans = [f[i][ord(labels[i]) - ord("a")] for i in range(n)]
        return ans

# https://leetcode.cn/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/339169/zi-shu-zhong-biao-qian-xiang-tong-de-jie-dian-sh-3