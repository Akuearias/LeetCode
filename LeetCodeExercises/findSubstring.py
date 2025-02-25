from itertools import permutations
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_words = len(words) * len(words[0])
        if len(s) < len_words:
            return []

        per = permutations(words)

        substrings = []
        for i in range(len(s) - len_words + 1):
            if s[i:i+len_words] in per:
                substrings.append(i)

        return substrings


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))