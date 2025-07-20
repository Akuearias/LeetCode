# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        tree = TreeNode(root_val)

        id_ = inorder.index(root_val)

        tree.right = self.buildTree(inorder[id_ + 1:], postorder)
        tree.left = self.buildTree(inorder[:id_], postorder)

        return tree