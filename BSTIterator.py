from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def InOrder(root, inorder):
            if not root:
                return
            InOrder(root.left, inorder)
            inorder.append(root.val)
            InOrder(root.right, inorder)

        self.root = root
        self.inorder = []
        InOrder(root, self.inorder)
        self.pointer = -1

    def next(self) -> int:
        self.pointer += 1
        return self.inorder[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.inorder) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()