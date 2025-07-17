def minTime(roads, machines):
    n = len(roads) + 1
    parent = [i for i in range(n)]
    has_machine = [False] * n
    for m in machines:
        has_machine[m] = True

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[rx] = ry
        has_machine[ry] = has_machine[ry] or has_machine[rx]
        return True

    # Sort roads by time descending
    roads.sort(key=lambda x: -x[2])

    total_cost = 0
    for u, v, time in roads:
        ru, rv = find(u), find(v)
        if has_machine[ru] and has_machine[rv]:
            # Cut the edge
            total_cost += time
        else:
            union(ru, rv)

    return total_cost