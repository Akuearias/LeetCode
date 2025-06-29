class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        dummy = self.head
        for _ in range(index):
            dummy = dummy.next

        return dummy.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, None)
        if not self.head:
            self.head = node
        else:
            dummy = self.head
            while dummy.next:
                dummy = dummy.next
            dummy.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        node = Node(val, cur.next)
        cur.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)