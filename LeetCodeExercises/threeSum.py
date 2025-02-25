from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        allSums = []
        for p1 in range(0, len(nums)):
            if p1 > 0 or nums[p1] != nums[p1 - 1]:
                p3 = len(nums) - 1
                for p2 in range(p1 + 1, len(nums)):
                    while p2 < p3 and nums[p1] + nums[p2] + nums[p3] > 0:
                        p3 -= 1
                    if p2 < p3 and nums[p1] + nums[p2] + nums[p3] == 0 and [nums[p1], nums[p2], nums[p3]] not in allSums:
                        allSums.append([nums[p1], nums[p2], nums[p3]])
        return allSums


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
