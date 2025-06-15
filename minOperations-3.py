from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = grid[0][0] % x
        S = 0
        nums = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != mod:
                    return -1

                else:
                    nums.append(grid[i][j])

        nums.sort()
        median = nums[len(nums) // 2]
        for num in nums:
            S += abs(num - median) // x
        return S


