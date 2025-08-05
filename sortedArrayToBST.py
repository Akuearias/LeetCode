from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BalancedBSTHelper(nums):
            if not nums:
                return None
            n = len(nums)
            root = TreeNode(nums[n//2])
            if len(nums) == 1:
                return root

            root.left = BalancedBSTHelper(nums[:n//2])
            root.right = BalancedBSTHelper(nums[n//2 + 1:])
            return root

        return BalancedBSTHelper(nums)
