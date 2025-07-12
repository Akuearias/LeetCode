def maxCircle(queries):
    parent = {}
    size = {}
    res = []
    max_size = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal max_size
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            if size[x_root] < size[y_root]:
                x_root, y_root = y_root, x_root
            parent[y_root] = x_root
            size[x_root] += size[y_root]
            max_size = max(max_size, size[x_root])

    for a, b in queries:
        for x in [a, b]:
            if x not in parent:
                parent[x] = x
                size[x] = 1
                max_size = max(max_size, 1)
        union(a, b)
        res.append(max_size)

    return res