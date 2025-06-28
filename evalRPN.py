from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        n = len(tokens)
        symbols = ['+', '-', '*', '/']
        while i < n:
            if tokens[i] in symbols:
                s1 = stack.pop()
                s2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(s2 + s1)
                elif tokens[i] == '-':
                    stack.append(s2 - s1)
                elif tokens[i] == '*':
                    stack.append(s2 * s1)
                else:
                    if s2 % s1 == 0:
                        stack.append(s2 // s1)
                    else:
                        if s1 * s2 >= 0:
                            stack.append(s2 // s1)
                        else:
                            stack.append(s2 // s1 + 1)
            else:
                stack.append(int(tokens[i]))
            i += 1

        return stack.pop()

if __name__ == '__main__':
    solution = Solution()
    assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22