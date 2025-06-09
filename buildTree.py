# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        tree = TreeNode(preorder[0])
        stack = [tree]
        id_ = 0

        for i in range(1, n):
            preorder_value = preorder[i]
            node = stack[-1]
            if node.val != inorder[id_]:
                node.left = TreeNode(preorder_value)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[id_]:
                    node = stack.pop()
                    id_ += 1
                node.right = TreeNode(preorder_value)
                stack.append(node.right)

        return tree
