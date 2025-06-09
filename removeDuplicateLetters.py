import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters_count = dict(collections.Counter(s))
        S = []
        in_ = set()
        for char in s:
            letters_count[char] -= 1
            if char in in_:
                continue

            while S and char < S[-1] and letters_count[S[-1]]:
                in_.remove(S.pop())
            S.append(char)
            in_.add(char)

        return ''.join(S)


