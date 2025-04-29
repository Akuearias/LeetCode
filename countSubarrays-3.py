'''

LeetCode Exercise #2962. Count Subarrays Where Max Element Appears at Least K Times

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.



Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5


'''
import collections
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''

        nums_count = dict(collections.Counter(nums))
        max_num = max(nums)
        if nums_count[max_num] < k:
            return 0

        else:
            S = 0
            for i in range(len(nums)):
                dummy = 0
                for j in range(i, len(nums)):
                    if nums[j] == max_num:
                        dummy += 1
                    if dummy >= k:
                        S += 1

            return S

        I can only think about the brute-force like this.

        '''
        n = len(nums)
        mx = max(nums)
        pos = [-1]
        for i in range(n):
            if nums[i] == mx:
                pos.append(i)
        left, right = 1, k
        ans = 0
        while right < len(pos):
            ans += (pos[left] - pos[left - 1]) * (n - pos[right])
            left += 1
            right += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    assert solution.countSubarrays([1,3,2,3,3], 2) == 6
    assert solution.countSubarrays([1,4,2,1], 3) == 0