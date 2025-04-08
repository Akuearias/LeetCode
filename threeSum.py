'''

LeetCode Exercise #15: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''

# This algorithm has a time complexity of O(n^2), but still can't pass.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        allSums = []
        for p1 in range(0, len(nums)):
            if p1 > 0 or nums[p1] != nums[p1 - 1]:
                p3 = len(nums) - 1
                for p2 in range(p1 + 1, len(nums)):
                    while p2 < p3 and nums[p1] + nums[p2] + nums[p3] > 0:
                        p3 -= 1
                    if p2 < p3 and nums[p1] + nums[p2] + nums[p3] == 0 and [nums[p1], nums[p2], nums[p3]] not in allSums:
                        allSums.append([nums[p1], nums[p2], nums[p3]])
        return allSums


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
