from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p0 = 0
        p1 = len(height) - 1
        max_area = 0
        while p0 != p1:
            max_area = max(max_area, min(height[p0], height[p1]) * (p1 - p0))
            if height[p0] < height[p1]:
                p0 += 1
            else:
                p1 -= 1
        return max_area


solution = Solution()
print(solution.maxArea([4,3,2,1,4]))