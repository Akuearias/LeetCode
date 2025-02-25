class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0
        if len(s) == 2:
            if s == '()':
                return 2
            else:
                return 0

        stack = []
        indices = []
        longest_valid = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                indices.append(i)
            else:
                if stack:
                    stack.pop()
                    indices.append(i)
                    longest_valid += 1

        return longest_valid * 2

solution = Solution()
print(solution.longestValidParentheses("()"))