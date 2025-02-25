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
