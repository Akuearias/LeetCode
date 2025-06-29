import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                total += nums[i]
            nums[i] = abs(nums[i])
        nums.sort()

        pq = [(nums[0], 0)]
        res = [0]

        while len(res) < k:
            curr_sum, idx = heapq.heappop(pq)
            res.append(curr_sum)

            if idx + 1 < len(nums):
                heapq.heappush(pq, (curr_sum - nums[idx] + nums[idx + 1], idx + 1))
                heapq.heappush(pq, (curr_sum + nums[idx + 1], idx + 1))

        return total - res[k - 1]
