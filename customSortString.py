import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        S = ''
        s_dict = dict(collections.Counter(s))
        for char in order:
            if char in s:
                for i in range(s_dict[char]):
                    S += char

        for char in s:
            if char not in order:
                S += char

        return S