from collections import deque


class MyQueue(object):
    def __init__(self):
        l1, l2 = [], []
        self.stack1 = deque(l1)
        self.stack2 = deque(l2)

    def peek(self):
        return self.stack1[0]

    def pop(self):
        self.stack2.pop()
        self.stack1.popleft()

    def put(self, value):
        self.stack1.append(value)
        self.stack2.appendleft(value)