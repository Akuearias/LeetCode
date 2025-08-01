import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.cn/problems/binary-tree-maximum-path-sum/solutions/297005/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-
class Solution:
    def __init__(self):
        self.S = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumHelper(node):
            if not node:
                return 0

            L = max(maxPathSumHelper(node.left), 0)
            R = max(maxPathSumHelper(node.right), 0)

            new = node.val + L + R

            self.S = max(self.S, new)

            return node.val + max(L, R)

        maxPathSumHelper(root)
        return self.S


