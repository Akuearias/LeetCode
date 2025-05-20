'''

LeetCode Exercise #41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-2^31 <= nums[i] <= 2^31 - 1

'''


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = 1
        for i in range(1, len(nums) + 1):
            if not nums_dict.get(i):
                return i
        return len(nums) + 1


solution = Solution()
assert solution.firstMissingPositive([1, 2, 0]) == 3
