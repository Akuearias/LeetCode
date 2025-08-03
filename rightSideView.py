from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        S = []
        queue = deque([root])
        visited = set()

        while queue:
            l = len(queue)
            for i in range(l):
                dummy = queue.popleft()
                if i == l - 1:
                    S.append(dummy.val)
                if dummy.left:
                    queue.append(dummy.left)
                if dummy.right:
                    queue.append(dummy.right)

        return S
