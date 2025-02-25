from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        original_listnode = []
        while head:
            original_listnode.append(head.val)
            head = head.next

        total = len(original_listnode)
        reverse = (total - total % k) // k

        remain = []
        if total % k != 0:
            remain = original_listnode[-(total % k):]


        reverse_list = []
        for i in range(0, reverse):
            reverse_list.append(original_listnode[(i*k):((i+1)*k)])

        result = []
        for listnode in reverse_list:
            for i in range(0, len(listnode)//2):
                obj = listnode[i]
                listnode[i] = listnode[len(listnode) - 1 - i]
                listnode[len(listnode) - 1 - i] = obj

            result += listnode

        result += remain

        reversed_listnode = ListNode()
        reversed_listnode_copy = reversed_listnode

        for i in range(len(result)):
            reversed_listnode_copy.val = result[i]
            if i != len(result) - 1:
                reversed_listnode_copy.next = ListNode()
                reversed_listnode_copy = reversed_listnode_copy.next

        return reversed_listnode


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, next=ListNode(2))
    reversed_head = solution.reverseKGroup(head, 2)
    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next
