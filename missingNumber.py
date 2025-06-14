'''

LeetCode Exercise #268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] == len(nums) - 1:
            return len(nums)

        elif nums[0] == 1:
            return 0

        L, R = 0, len(nums) - 1
        while L < R:
            m = (L + R) // 2
            if nums[m] != m:
                R = m

            else:
                L = m + 1

        return L
