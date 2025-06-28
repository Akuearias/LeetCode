import math


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        DP = [0] * n
        DP[0] = 9
        for i in range(1, n):
            DP[i] = 9 * math.factorial(9) // math.factorial(9 - i) + DP[i - 1]
        return DP[-1] + 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.countNumbersWithUniqueDigits(3) == 739