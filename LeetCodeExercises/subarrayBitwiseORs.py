from itertools import combinations
from typing import List
from functools import reduce

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        S = 0

        i = 0

        while i < len(arr):
            start = arr[i]
            max_val = start
            for j in range(i, len(arr)):
                start |= arr[j]
                if start > max_val:
                    max_val = start
                    S += 1

            i += 1

        return S




solution = Solution()
print(solution.subarrayBitwiseORs([1,1,2]))
