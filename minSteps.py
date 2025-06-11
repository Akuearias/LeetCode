class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {chr(ord('a') + i):0 for i in range(26)}
        t_dict = {chr(ord('a') + i):0 for i in range(26)}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        s_counts = list(s_dict.values())
        t_counts = list(t_dict.values())

        S = 0
        for i in range(26):
            S += abs(s_counts[i] - t_counts[i])

        return S // 2