class Solution:
    def numDecodings(self, s: str) -> int:
        codes = [1] + [0] * len(s)
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                codes[i] += codes[i - 1]
            if i > 1:
                if s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                    codes[i] += codes[i - 2]

        return codes[-1]
