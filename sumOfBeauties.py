'''

LeetCode Exercise #2012: Sum of Beauty in the Array

You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
Example 2:

Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.


Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 105

'''
from typing import List

# Here I learned that using status "flags" are useful in some cases, making the algorithm simpler, reducing iterations.
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        S = 0
        flags = [0] * len(nums)
        max_val = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] > max_val:
                flags[i] = 1
                max_val = nums[i]

        min_val = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if flags[i] == 1 and nums[i] < min_val:
                S += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                S += 1
            min_val = min(min_val, nums[i])

        return S

if __name__ == '__main__':
    solution = Solution()
    assert solution.sumOfBeauties([1, 2, 3]) == 2
    assert solution.sumOfBeauties([2, 4, 6, 4]) == 1
    assert solution.sumOfBeauties([3, 2, 1]) == 0
