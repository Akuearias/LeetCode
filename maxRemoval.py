'''

LeetCode Exercise #3362. Zero Array Transformation III

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.



Example 1:

Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:

Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].

Example 3:

Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.



Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= li <= ri < nums.length

'''
import heapq
from typing import List

# Key points: Greedy, Sorting, Heap/Priority Queue.
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])

        n = len(nums)
        diff = [0] * (n + 1)

        heap = []

        dummy = 0  # Dummy value for difference array
        dummy_2 = 0  # Pointer

        for i, num in enumerate(nums):
            dummy += diff[i]
            while dummy_2 < len(queries) and queries[dummy_2][0] == i:
                heapq.heappush(heap, -queries[dummy_2][1])
                dummy_2 += 1

            while dummy < num and heap and -heap[0] >= i:
                dummy += 1
                diff[-heapq.heappop(heap) + 1] -= 1

            if num - dummy > 0:
                return -1

        return len(heap)


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]) == 1
    assert solution.maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]) == 2
    assert solution.maxRemoval(nums = [1,2,3,4], queries = [[0,3]]) == -1