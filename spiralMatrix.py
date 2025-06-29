from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        x, y = 0, 0
        w, s, a, d = 0, m - 1, 0, n - 1
        while head:
            matrix[x][y] = head.val
            if x == w and y < d:
                y += 1
                if y == d:
                    w += 1
            elif y == d and x < s:
                x += 1
                if x == s:
                    d -= 1
            elif x == s and y > a:
                y -= 1
                if y == a:
                    s -= 1
            elif y == a and x > w:
                x -= 1
                if x == w:
                    a += 1
            head = head.next

        return matrix
