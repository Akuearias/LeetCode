from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        S = []

        def preOrder(root, S):
            if root:
                S.append(root.val)
                preOrder(root.left, S)
                preOrder(root.right, S)
            else:
                return

        if not root:
            return

        if not root.left and not root.right:
            return

        preOrder(root, S)
        root_copy = root
        for i in range(1, len(S)):
            root_copy.left = None
            root_copy.right = TreeNode(S[i])
            root_copy = root_copy.right


