import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        alphabet = [chr(ord('a') + i) for i in range(26)]
        queue = collections.deque([(beginWord, 1)])
        visited = set([beginWord])
        n = len(beginWord)

        while queue:
            curr, S = queue.popleft()
            if curr == endWord:
                return S

            for i in range(n):
                for a in alphabet:
                    if curr[i] == a:
                        continue
                    mod = curr[:i] + a + curr[i + 1:]
                    if mod in wordSet and mod not in visited:
                        visited.add(mod)
                        queue.append((mod, S + 1))

        return 0
