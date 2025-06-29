import collections
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_dict = collections.defaultdict(list)
        for r in richer:
            richer_dict[r[1]].append(r[0])

        S = [None] * len(quiet)

        def DFS(person):
            if S[person]:
                return

            S[person] = person
            for i in richer_dict[person]:
                DFS(i)
                if quiet[S[i]] < quiet[S[person]]:
                    S[person] = S[i]

        for j in range(len(quiet)):
            DFS(j)

        return S

# https://leetcode.cn/problems/loud-and-rich/solutions/1156924/xuan-nao-he-fu-you-by-leetcode-solution-jnzm
