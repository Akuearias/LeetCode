'''

LeetCode Exercise # 416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

HINT: According to the official solution, this is an NP-hard problem, and therefore
we should not expect a solution with polynomial-level time complexity.

'''

# HINT: According to the official solution, this is an NP-hard problem, and therefore
# we should not expect a solution with polynomial-level time complexity.

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        dummy = sum(nums)
        if dummy % 2 != 0:
            return False

        if dummy // 2 < max(nums):
            return False

        DP_list = [[False] * (dummy//2+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            DP_list[i][0] = True

        DP_list[0][nums[0]] = True

        for i in range(len(nums)):
            for j in range(dummy // 2 + 1):
                if j >= nums[i]:
                    DP_list[i][j] = DP_list[i - 1][j] | DP_list[i - 1][j - nums[i]]
                else:
                    DP_list[i][j] = DP_list[i - 1][j]

        return DP_list[len(nums) - 1][dummy // 2]


if __name__ == '__main__':
    solution = Solution()
    assert solution.canPartition([1, 5, 11, 5]) == True
    assert solution.canPartition([1, 2, 3, 5]) == False
    assert solution.canPartition([2, 2, 3, 5]) == False