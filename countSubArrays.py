'''

LeetCode Exercise #2444. Count Subarrays With Fixed Bounds

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.


Constraints:

2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6

'''
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        sub_arrays = []
        dummy = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                sub_arrays.append(nums[dummy:i])
                dummy = i + 1
        sub_arrays.append(nums[dummy:])

        S = 0

        for sub_array in sub_arrays:
            dummy = -1
            dummy_L, dummy_R = None, None
            for i in range(len(sub_array)):
                if sub_array[i] == minK:
                    dummy_L = i
                if sub_array[i] == maxK:
                    dummy_R = i

                if dummy_L is not None and dummy_R is not None:
                    s = min(dummy_L, dummy_R) - dummy
                    S += s

        return S

if __name__ == '__main__':
    solution = Solution()
    assert solution.countSubarrays([1,3,5,2,7,5], 1, 5) == 2
    assert solution.countSubarrays([1, 1, 1, 1], 1, 1) == 10