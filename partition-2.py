from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.cn/problems/partition-list/solutions/543768/fen-ge-lian-biao-by-leetcode-solution-7ade
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s = ListNode(0)
        small_head = s
        l = ListNode(0)
        large_head = l
        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                l.next = head
                l = l.next
            head = head.next

        l.next = None
        s.next = large_head.next
        return small_head.next

