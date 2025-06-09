from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd Alg
        p1, p2 = nums[0], nums[0]
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break

        p1 = nums[0]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1

