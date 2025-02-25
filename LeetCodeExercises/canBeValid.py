class Solution:
    def Valid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return True

    def canBeValidHelper(self, s, unlock_i) -> bool:
        if s[unlock_i] == '(':
            changed = ')'
            B1 = self.Valid(s)
            return B1 or self.Valid(s[:unlock_i] + changed + s[unlock_i + 1:])

        else:
            changed = '('
            B2 = self.Valid(s)
            return B2 or self.Valid(s[:unlock_i] + changed + s[unlock_i + 1:])


    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        else:
            unlock = []
            for i in range(len(locked)):
                if locked[i] == '0':
                    unlock.append(i)

            B = False
            for unlock_i in unlock:
                B = B or self.canBeValidHelper(s, unlock_i)

            return B


if __name__ == "__main__":
    solution = Solution()
    print(solution.canBeValid("))()))", "010100"))