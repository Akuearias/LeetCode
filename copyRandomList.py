from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    nodeDict = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head not in self.nodeDict:
            node = Node(head.val)
            self.nodeDict[head] = node
            node.next = self.copyRandomList(head.next)
            node.random = self.copyRandomList(head.random)

        return self.nodeDict[head]

