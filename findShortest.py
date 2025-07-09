from collections import defaultdict, deque


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    if ids.count(val) < 2:
        return -1
    
    graph = defaultdict(list)
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)

    sources = [i + 1 for i, color in enumerate(ids) if color == val]

    queue = deque()
    visited_by = {}
    distance = {}

    for s in sources:
        queue.append((s, 0))
        visited_by[s] = s
        distance[s] = 0

    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited_by:
                visited_by[neighbor] = visited_by[node]
                distance[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
            else:
                if visited_by[neighbor] != visited_by[node]:
                    return distance[neighbor] + dist + 1

    return -1
