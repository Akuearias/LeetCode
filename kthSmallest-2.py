from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, S):
            if not root:
                return
            inOrder(root.left, S)
            S.append(root.val)
            inOrder(root.right, S)

        if not root.left and not root.right:
            return root.val

        S = []
        inOrder(root, S)
        return S[min(k - 1, len(S) - 1)]
