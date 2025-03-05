'''

Leetcode #55 Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

'''

# I used to meet many problems in this exercise. However, after learning about DP, I solved it.
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if len(nums) > 1 and nums[0] == 0:
            return False

        dp_table = [False] * len(nums)

        dp_table[-1] = True
        destination = len(nums) - 1

        for i in range(len(dp_table) - 2, -1, -1):
            if destination - i <= nums[i]:
                dp_table[i] = True
                destination = i

        return dp_table[0]


solution = Solution()
assert solution.canJump([1,0,1,0]) == False
