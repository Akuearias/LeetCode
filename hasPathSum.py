from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSumHelper(root, targetSum):
            if not root.left and not root.right:
                return root.val == targetSum
            B1, B2 = False, False
            if not (not root.left and not root.right):
                if root.left:
                    B1 = self.hasPathSum(root.left, targetSum - root.val)
                if root.right:
                    B2 = self.hasPathSum(root.right, targetSum - root.val)
            return B1 or B2

        if not root:
            return False
        return hasPathSumHelper(root, targetSum)