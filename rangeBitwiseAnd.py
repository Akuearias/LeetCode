class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left

        l1 = len(bin(left)[2:])
        l2 = len(bin(right)[2:])

        b1, b2 = list(bin(left)[2:]), list(bin(right)[2:])
        b1 = ['0' for _ in range(len(b2) - len(b1))] + b1
        stack = []
        for i in range(len(b2) - 1, -1, -1):
            if right - left <= 2 ** (len(b2) - 1 - i) - 1:
                if b1[i] == b2[i] == '1':
                    stack.append('1')
                else:
                    stack.append('0')
            else:
                stack.append('0')

        S = []
        while stack:
            S.append(stack.pop())
        return int(''.join(S), base=2) if len(S) > 0 else 0