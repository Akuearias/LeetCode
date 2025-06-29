from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.S = 0

        def DFS(tree):
            if not tree:
                return []

            if not tree.left and not tree.right:
                return [1]

            L = DFS(tree.left)
            R = DFS(tree.right)

            for l in L:
                for r in R:
                    if l + r <= distance:
                        self.S += 1

            return [d + 1 for d in L + R if d + 1 <= distance]

        DFS(root)
        return self.S

