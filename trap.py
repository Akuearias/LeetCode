'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

'''
from typing import List

# Key words: Stack, Array, Two Pointers, DP, Monotonic Stack.
'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

'''


# Key words: Stack, Array, Two Pointers, DP, Monotonic Stack.
# Here in this case: max prefix & max suffix
class Solution:
    def trap(self, height: List[int]) -> int:
        S = 0
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        maxL[0] = height[0]
        maxR[-1] = height[-1]

        for i in range(1, len(height)):
            maxL[i] = max(maxL[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])

        for j in range(len(height)):
            S += min(maxL[j], maxR[j]) - height[j]

        return S



solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
