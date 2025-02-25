import collections


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        B = False
        stack = []
        for i in s:
            if s[0] == ')' or s[0] == ']' or s[0] == '}':
                return False
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            if i == ")" or i == "]" or i == "}":
                if stack and stack[-1] == '(' and i == ')':
                    stack.pop()
                    B = True
                    continue

                elif stack and stack[-1] == '[' and i == ']':
                    stack.pop()
                    B = True
                    continue

                elif stack and stack[-1] == '{' and i == '}':
                    stack.pop()
                    B = True
                    continue
                else:
                    if stack:
                        stack.pop()
                    B = False
                    break

        if not stack and B:
            B = True
        else:
            B = False
        return B

if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("()") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([])") is True
    assert solution.isValid("}{") is False
    assert solution.isValid("()[]}{") is False
    assert solution.isValid("([)]") is False
    assert solution.isValid("((") is False
    assert solution.isValid("({{{{}}}))") is False
    assert solution.isValid("[[[]") is False



