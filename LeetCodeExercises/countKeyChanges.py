class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        s = s.lower()
        last_char = s[0]
        for i in range(1, len(s)):
            if s[i] != last_char:
                count += 1
            last_char = s[i]

        return count
