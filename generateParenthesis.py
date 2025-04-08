'''

LeetCode Exercise #22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

'''

# Backtracking algorithm example
from typing import List, Optional


class Solution:

    def generateParenthesisHelper(self, all_pars: [], par: str, n: int, L: int, R: int):
        if L == R and L + R == 2*n:
            all_pars.append(par)
            return
        else:
            if L < n:
                self.generateParenthesisHelper(all_pars, par + "(", n, L + 1, R)
            if R < L:
                self.generateParenthesisHelper(all_pars, par + ")", n, L, R + 1)
            else:
                return

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        else:
            all_pars = []
            self.generateParenthesisHelper(all_pars, "", n, 0, 0)
            return all_pars

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
