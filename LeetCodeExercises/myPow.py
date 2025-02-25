class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0 and n == 0:
            return
        if int(x) != 0 and n == 0:
            return 1
        else:
            if n > 0:
                if n == 1:
                    return x
                else:
                    if n % 2 == 0:
                        return self.myPow(x, n//2) * self.myPow(x, n//2)
                    else:
                        return self.myPow(x, n//2) * self.myPow(x, n//2 + 1)
            else:
                if n == -1:
                    return 1/x
                else:
                    if n % 2 == 0:
                        return self.myPow(x, n//2) * self.myPow(x, n//2)
                    else:
                        return self.myPow(x, n//2) * self.myPow(x, n//2 + 1)


solution = Solution()
print(solution.myPow(2.00, 10))
