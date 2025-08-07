class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            if n % 2 == 1:
                return self.hammingWeight(n // 2) + 1
            else:
                return self.hammingWeight(n // 2)