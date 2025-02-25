# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def DFS(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.DFS(head.next, root.left) or self.DFS(head.next, root.right)


    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.DFS(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)






if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, next=ListNode((4), next=ListNode(2, next=ListNode(6, next=None))))
    root = TreeNode(1, left=TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
                    right=TreeNode(4, left=TreeNode(2, left=TreeNode(6), right=TreeNode(8, left=TreeNode(1), right=TreeNode(3)))))
    print(solution.isSubPath(head, root))
