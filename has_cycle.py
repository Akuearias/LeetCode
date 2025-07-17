class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    visited = set()
    visited.add(head)
    while head:
        if head.next not in visited:
            head = head.next
            if head:
                visited.add(head)
        else:
            return True
    return False