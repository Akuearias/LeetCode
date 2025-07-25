# https://leetcode.com/problems/short-encoding-of-words/solutions/127519/short-encoding-of-words
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            for k in range(1, len(word)):
                words_set.discard(word[k:])

        return sum(len(word) + 1 for word in words_set)
