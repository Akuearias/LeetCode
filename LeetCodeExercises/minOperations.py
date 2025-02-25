from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        S = 0
        nums.sort()
        heapq.heapify(nums)

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            S += 1
            heapq.heappush(nums, z)

        return S

solution = Solution()
# assert solution.minOperations([2, 11, 10, 1, 3], 10) == 2
# assert solution.minOperations([1, 1, 2, 4, 9], 20) == 4
assert solution.minOperations([15,90,76,23,66,28,37,16,45], 91) == 6

