class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPowHelper(x, n):
            if n == 1:
                return x
            dummy = myPowHelper(x, n // 2)
            if n % 2 == 0:
                return dummy * dummy
            else:
                return x * dummy * dummy

        if n == 0 and x != 0:
            return 1
        if x == 0 or x == 1:
            return x
        if x == -1:
            return 1 if n % 2 == 0 else -1

        if n > 0:
            return myPowHelper(x, n)
        else:
            return 1 / myPowHelper(x, -n)
