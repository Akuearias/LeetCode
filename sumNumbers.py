from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        def numCollector(root, nums, num):
            num.append(str(root.val))
            if not root.left and not root.right:
                nums.append(''.join(num))
            else:
                if root.left:
                    numCollector(root.left, nums, num[:])
                if root.right:
                    numCollector(root.right, nums, num[:])

        num = []
        numCollector(root, nums, num)
        S = 0
        for n in nums:
            S += int(n)

        return S

