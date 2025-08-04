from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/word-search-ii/solutions/1000172/dan-ci-sou-suo-ii-by-leetcode-solution-7494
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        curr = self
        for w in word:
            curr = curr.children[w]
        curr.is_word = True
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def DFS(curr, i, j):
            if board[i][j] not in curr.children:
                return

            dummy = board[i][j]

            curr = curr.children[dummy]
            if curr.word != "":
                S.add(curr.word)

            board[i][j] = "."
            for i1, j1 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= i1 < m and 0 <= j1 < n:
                    DFS(curr, i1, j1)
            board[i][j] = dummy

        S = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                DFS(trie, i, j)

        return list(S)
