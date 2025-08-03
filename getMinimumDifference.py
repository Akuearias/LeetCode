from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifferenceHelper(self, root, S):
        if not root:
            return

        S.append(root.val)
        self.getMinimumDifferenceHelper(root.left, S)
        self.getMinimumDifferenceHelper(root.right, S)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        S = []
        self.getMinimumDifferenceHelper(root, S)

        S.sort()
        min_ = math.inf
        for i in range(1, len(S)):
            min_ = min(min_, S[i] - S[i - 1])

        return min_
