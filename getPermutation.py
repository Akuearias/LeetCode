import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        k -= 1
        res = ""

        for i in range(n, 0, -1):
            group_len = math.factorial(i - 1)
            index = k // group_len
            res += str(nums[index])
            nums.pop(index)
            k %= group_len

        return res