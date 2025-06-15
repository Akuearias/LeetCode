from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate the length of the listnode
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Calculate the number of valid steps
        k = k % length
        if k == 0:
            return head

        # Step 3: Make a loop
        tail.next = head

        # Step 4: Find the tail and break the loop
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
