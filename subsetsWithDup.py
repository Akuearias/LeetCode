from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        stack = []

        def DFS(pre, curr):
            if curr == len(nums):
                subsets.append(stack[:])
                return

            DFS(False, curr + 1)
            if not pre and curr > 0 and nums[curr] == nums[curr - 1]:
                return

            stack.append(nums[curr])
            DFS(True, curr + 1)
            stack.pop()

        DFS(False, 0)
        return subsets