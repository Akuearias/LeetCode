class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        if dividend == 0:
            return 0
        if dividend > 2**31 - 1:
            dividend = 2**31 - 1
        if dividend < -2**31:
            dividend = -2**31
        if divisor == 1:
            return dividend
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            a -= b
            q += 1
        if dividend * divisor < 0:
            q *= -1
        if q < -2**31:
            q = -2**31
        elif q > 2**31 - 1:
            q = 2**31 - 1
        return q