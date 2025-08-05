from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr = dummy
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        curr.next = head1 or head2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        H1, H2 = head, head
        while H2.next and H2.next.next:
            H1 = H1.next
            H2 = H2.next.next

        H3 = H1.next
        H1.next = None

        left = self.sortList(head)
        right = self.sortList(H3)

        return self.merge(left, right)

