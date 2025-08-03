import collections
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        genes = ['A', 'C', 'G', 'T']
        queue = collections.deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            curr, S = queue.popleft()
            if curr == endGene:
                return S

            for i in range(8):
                for g in genes:
                    if curr[i] == g:
                        continue
                    mut = curr[:i] + g + curr[i + 1:]
                    if mut in bankSet and mut not in visited:
                        visited.add(mut)
                        queue.append((mut, S + 1))

        return -1