'''

LeetCode Exercise #2799. Count Complete Subarrays in an Array

You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.



Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2000

'''
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # The commented code below is a brute-force one, with time complexity of O(n^2).
        '''
        nums_set = set(nums)
        N = len(nums_set)
        S = 0
        for i in range(0, len(nums) - N + 1):
            for j in range(i + N, len(nums)+1):
                if len(set(nums[i:j])) == N:
                    S += 1

        return S
        '''
        # The code below is the one from solution. Though I read the words explaining it, I still cannot catch the point.
        # Time complexity: O(n)
        # Key words: sliding window
        k = len(set(nums))
        S = 0
        count = {}
        R = 0
        for L in range(len(nums)):
            if L > 0:
                dummy = nums[L - 1]
                count[dummy] -= 1
                if count[dummy] == 0:
                    count.pop(dummy)

            while R < len(nums) and len(count) < k:
                add = nums[R]
                count[add] = count.get(add, 0) + 1
                R += 1

            if len(count) == k:
                S += (len(nums) - R + 1)

        return S

if __name__ == '__main__':
    solution = Solution()
    assert solution.countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
    assert solution.countCompleteSubarrays([5, 5, 5, 5]) == 10