from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m = len(grid)
        curr = grid[0][0]
        isLeaf = True
        for i in range(m):
            for j in range(m):
                if grid[i][j] != curr:
                    isLeaf = False
                    break
        if isLeaf:
            return Node(curr, isLeaf, None, None, None, None)
        else:
            return Node(curr, isLeaf, self.construct([row[:m//2] for row in grid[:m//2]]),
                                      self.construct([row[m//2:] for row in grid[:m//2]]),
                                      self.construct([row[:m//2] for row in grid[m//2:]]),
                                      self.construct([row[m//2:] for row in grid[m//2:]]))