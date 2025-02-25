import math


class Solution:
    def reverse(self, x: int) -> int:
        if 0 <= abs(x) < 10:
            return x
        str_x = list(str(abs(x)))
        for i in range(0, len(str_x)//2):
            str_x[i] = str_x[len(str_x)-i-1]
        num = int(''.join(str_x))
        if num < math.pow(-2, 31) or num > math.pow(2, 31) - 1:
            return 0
        if x < 0:
            return -num
        else:
            return num