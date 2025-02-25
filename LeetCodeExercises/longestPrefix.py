class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix = ""
        for i in range(1, len(s)):
            left = s[0:i]
            right = s[len(s)-i:len(s)]
            if left == right:
                prefix = left
        return prefix


if __name__ == "__main__":
    s = "ababab"
    print(Solution().longestPrefix(s))