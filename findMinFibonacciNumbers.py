class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        Fibo = []
        Fibo.append(1)
        Fibo.append(1)
        while Fibo[-1] + Fibo[-2] <= k:
            Fibo.append(Fibo[-1] + Fibo[-2])

        S = 0
        count = 0
        while Fibo:
            curr = Fibo.pop()
            if S + curr <= k:
                S += curr
                count += 1
        return count
