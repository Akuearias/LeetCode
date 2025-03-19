from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            return [nums] if sum(nums) == target else []

        nums.sort()
        if nums[0] == nums[len(nums) - 1]:
            return [nums[0:4]] if sum(nums[0:4]) == target else []
        results = []
        for p1 in range(0, len(nums) - 1):
            if p1 > 0 or nums[p1] != nums[p1 - 1]:
                p4 = len(nums) - 1
                for p2 in range(p1 + 1, len(nums)):
                    for p3 in range(p2 + 1, len(nums)):
                        while p3 < p4 and nums[p1] + nums[p2] + nums[p3] + nums[p4] > target:
                            p4 -= 1
                        if p3 < p4 and nums[p1] + nums[p2] + nums[p3] + nums[p4] == target and not [nums[p1], nums[p2], nums[p3], nums[p4]] in results:
                            results.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        if p3 == p4 and p4 != len(nums) - 1:
                            p4 = len(nums) - 1

        return results


if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0))