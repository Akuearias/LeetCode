import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [nums[i] * -1 for i in range(len(nums))]
        nums.sort()
        heapq.heapify(nums)

        largest = []
        for i in range(k):
            largest.append(heapq.heappop(nums))

        return -1 * largest.pop()


solution = Solution()
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
