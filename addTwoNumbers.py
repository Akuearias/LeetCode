# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        s1, s2 = "", ""
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1:
            s1 += str(stack1.pop())

        while stack2:
            s2 += str(stack2.pop())

        s1, s2 = int(s1), int(s2)
        S = s1 + s2
        S = list(str(S))
        listnode = ListNode()
        Dummy = ListNode('dummy', listnode)
        Dummy = Dummy.next
        while S:
            listnode.val = int(S.pop())
            if S:
                listnode.next = ListNode()
                listnode = listnode.next
        return Dummy
