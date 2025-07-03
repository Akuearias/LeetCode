# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        linkedlist2 = ListNode(None, head)
        dummy = linkedlist2.next
        visited = set()
        while dummy:
            if dummy not in visited:
                visited.add(dummy)
                dummy = dummy.next
            else:
                return dummy

        return None
