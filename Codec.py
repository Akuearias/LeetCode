# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return []
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        return ' '.join(preorder(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = list(map(int, data.split()))

        def insert(root, val):
            if not root:
                return TreeNode(val)

            if val < root.val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root

        S = None
        for val in vals:
            S = insert(S, val)

        return S

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans