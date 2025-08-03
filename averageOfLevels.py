from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        S = []
        queue = deque([root])

        while queue:
            dummy = 0
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                dummy += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            S.append(dummy / l)

        return S
