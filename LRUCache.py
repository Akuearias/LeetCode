class DoubleLinkedList:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash = {}

    def get(self, key: int) -> int:
        if key in self.hash:
            dummy = self.hash[key]
            self.moveToHead(dummy)
            return self.hash[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            node = DoubleLinkedList(key, value)
            self.hash[key] = node
            self.addToHead(node)

            if len(self.hash) > self.capacity:
                dummy = self.removeTail()
                self.hash.pop(dummy.key)

        else:
            node = self.hash[key]
            node.val = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# https://leetcode.cn/problems/lru-cache/solutions/259678/lruhuan-cun-ji-zhi-by-leetcode-solution/

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)