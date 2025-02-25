from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numList = nums
        for i in range(k):
            tail = [numList[len(numList) - 1]]
            nums.remove(numList[len(numList) - 1])
            numList = tail + numList
            nums = numList


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 3)
print(nums)
