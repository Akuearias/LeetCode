from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        def find(target, i, nums):
            for n in range(len(nums)):
                if nums[n] + n >= target:
                    i += 1
                    target = n
                    break
            return (target, i)

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] == 0:
                return 0
            else:
                return 1

        target = len(nums) - 1
        i = 0
        while target != 0:
            tup = find(target, i, nums)
            target = tup[0]
            i = tup[1]
        return i




solution = Solution()
nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
# nums = [2, 3, 1, 1, 4]
print(solution.jump(nums))
