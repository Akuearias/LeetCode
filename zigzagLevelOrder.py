# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        S = []
        queue = [root]
        queue = collections.deque(queue)
        visited = set()

        while queue:
            curr = []
            for _ in range(len(queue)):
                dummy = queue.popleft()
                curr.append(dummy.val)
                if dummy.left:
                    queue.append(dummy.left)
                if dummy.right:
                    queue.append(dummy.right)
            S.append(curr)

        for i in range(len(S)):
            if i % 2 != 0:
                S[i].reverse()

        return S
