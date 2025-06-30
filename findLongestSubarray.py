from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        S = [[0, 0] for _ in range(len(array) + 1)]
        max_ = 0
        L = 0
        for i in range(len(array)):
            S[i + 1] = S[i][:]
            try:
                int(array[i])
                S[i + 1][1] += 1
            except ValueError:
                S[i + 1][0] += 1

        diffs = {}
        for i in range(len(S)):
            if S[i][1] - S[i][0] not in diffs:
                diffs[S[i][1] - S[i][0]] = i
            else:
                R = i
                if R - diffs[S[i][1] - S[i][0]] > max_:
                    max_ = R - diffs[S[i][1] - S[i][0]]
                    L = diffs[S[i][1] - S[i][0]]

        return array[L:L + max_]
