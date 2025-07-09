from collections import deque


def swapNodes(indexes, queries):
    def inorder_iterative(root):
        res = []
        stack = []
        curr = root
        while curr != -1 or stack:
            while curr != -1:
                stack.append(curr)
                curr = indexes[curr - 1][0]
            curr = stack.pop()
            res.append(curr)
            curr = indexes[curr - 1][1]
        return res

    def swap_at_depth_bfs(k):
        queue = deque([(1, 1)])  # (node, depth)
        while queue:
            node, depth = queue.popleft()
            if node == -1:
                continue
            if depth % k == 0:
                indexes[node - 1][0], indexes[node - 1][1] = indexes[node - 1][1], indexes[node - 1][0]
            left, right = indexes[node - 1]
            queue.append((left, depth + 1))
            queue.append((right, depth + 1))

    result = []
    for k in queries:
        swap_at_depth_bfs(k)
        traversal = inorder_iterative(1)
        result.append(traversal)
    return result