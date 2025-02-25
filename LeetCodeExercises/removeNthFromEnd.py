from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        all_nodes = []
        while head:
            all_nodes.append(head.val)
            head = head.next

        all_nodes = all_nodes[0:len(all_nodes) - n] + all_nodes[len(all_nodes) - n + 1:]

        new_listNode = ListNode(all_nodes.pop(0))
        new_listNode_copy = new_listNode
        while all_nodes:
            new_listNode_copy.next = ListNode()
            new_listNode_copy = new_listNode_copy.next
            new_listNode_copy.val = all_nodes.pop(0)

        return new_listNode


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(4, next=ListNode(5, next=ListNode(4, next=None)))
    new_head = solution.removeNthFromEnd(head, 1)
    while new_head:
        print(new_head.val)
        new_head = new_head.next

