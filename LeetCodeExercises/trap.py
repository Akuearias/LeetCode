from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        S = 0
        i = 0
        while i < len(height) - 2:
            slot = 1
            pointer = i + 2
            while height[i] > height[pointer]:
                pointer += 1
                slot += 1
            for j in range(i+1, pointer):
                S += min(height[i], height[pointer]) - height[j]

            i += slot
        return S


solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
