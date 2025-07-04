# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.countNodesHelper(root)

    def countNodesHelper(self, root) -> int:
        if not root:
            return 0
        else:
            return 1 + self.countNodesHelper(root.left) + self.countNodesHelper(root.right)