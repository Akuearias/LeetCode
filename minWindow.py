import collections
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ''

        goal = collections.Counter(t)
        window = {}
        l = 0
        r = 0
        valid = 0
        start = 0

        min_ = math.inf

        while r < len(s):
            char = s[r]
            r += 1

            if char in goal:
                window[char] = window.get(char, 0) + 1
                if window[char] == goal[char]:
                    valid += 1
            while valid == len(goal):
                if r - l < min_:
                    dummy = l
                    min_ = r - l

                d = s[l]
                l += 1
                if d in goal:
                    if window[d] == goal[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_ == math.inf else s[dummy:dummy + min_]

