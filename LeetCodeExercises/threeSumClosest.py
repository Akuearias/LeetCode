import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        three_sum = math.inf
        nums.sort()
        s1, s2, s3 = None, None, None
        for p1 in range(0, len(nums)):
            s1 = nums[p1]
            if p1 > 0 or nums[p1] != nums[p1 - 1]:
                p3 = len(nums) - 1
                s3 = nums[p3]
                for p2 in range(p1 + 1, len(nums)):
                    if p2 == p3:
                        break
                    s2 = nums[p2]
                    if abs(s1 + s2 + s3 - target) < abs(three_sum - target):
                        three_sum = s1 + s2 + s3
                    while p2 < p3 and abs(s1 + s2 + s3 - target) >= abs(nums[p1] + nums[p2] + nums[p3-1] - target):
                        p3 -= 1
                        if p2 < p3:
                            s3 = nums[p3]
                            if abs(s1 + s2 + s3 - target) < abs(three_sum - target):
                                three_sum = s1 + s2 + s3

        return three_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-4,2,2,3,3,3], 0))

