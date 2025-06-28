# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def isSufficient(sum_, node, limit):
            if not node:
                return False

            if not node.left and not node.right:
                return node.val + sum_ >= limit

            sufficientL, sufficientR = isSufficient(sum_ + node.val, node.left, limit), isSufficient(sum_ + node.val,
                                                                                                     node.right, limit)
            if not sufficientL:
                node.left = None
            if not sufficientR:
                node.right = None

            return sufficientL or sufficientR

        return root if isSufficient(0, root, limit) else None

# https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/solutions/2276391/gen-dao-xie-lu-jing-shang-de-bu-zu-jie-d-f4vz