'''

LeetCode Exercise #209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4


'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        dummy = nums[0]
        prefix_sums = [0, dummy]
        for i in range(1, len(nums)):
            dummy += nums[i]
            prefix_sums.append(dummy)

        S = len(nums) + 1
        for i in range(1, len(nums) + 1):
            sum_ = target + prefix_sums[i - 1]
            B = bisect.bisect_left(prefix_sums, sum_)
            if B != len(prefix_sums):
                S = min(S, B - (i - 1))

        return 0 if S == len(nums) + 1 else S