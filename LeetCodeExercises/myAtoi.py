class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 or (not s[0].isnumeric() and s[0] != '-' and s[0] != '+'):
            return 0
        if s[0] == '-':
            if not s[1].isnumeric():
                return 0
            else:
                prefix = s[0]
                for i in range(1, len(s)):
                    if s[i].isnumeric():
                        prefix += s[i]
                    else:
                        break
                num = int(prefix)
                if num < -2147483648:
                    num = -2147483648
                return num
        elif s[0] == '+' or s[0].isnumeric():
            if s[0] == "+" and not s[1].isnumeric():
                return 0 if not s[1].isnumeric() else s[0]
            prefix = s[0]
            for i in range(1, len(s)):
                if s[i].isnumeric():
                    prefix += s[i]
                else:
                    break
            num = int(prefix)
            if num > 2147483647:
                num = 2147483647
            return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("3.14159"))
