class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [0] * len(s)
        for i in range(len(s)):
            diff[i] = abs(ord(t[i]) - ord(s[i]))

        i = 0
        S = 0
        Count = 0
        for j in range(len(s)):
            S += abs(ord(t[j]) - ord(s[j]))

            while S > maxCost:
                S -= abs(ord(t[i]) - ord(s[i]))
                i += 1

            Count = max(Count, j - i + 1)

        return Count
