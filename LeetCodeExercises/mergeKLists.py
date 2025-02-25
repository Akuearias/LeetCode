from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        all_nodes = []
        for listnode in lists:
            while listnode:
                all_nodes.append(listnode.val)
                listnode = listnode.next
        
        all_nodes.sort()
        new_listNode = ListNode(all_nodes.pop(0))
        new_listNode_copy = new_listNode

        while all_nodes:
            new_listNode_copy.next = ListNode()
            new_listNode_copy = new_listNode_copy.next
            new_listNode_copy.val = all_nodes.pop(0)

        return new_listNode