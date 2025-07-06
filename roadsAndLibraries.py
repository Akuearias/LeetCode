from collections import defaultdict, deque


# Still weak in solving graph problems.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n * c_lib

    adj = defaultdict(list)
    for u, v in cities:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    total_cost = 0

    def bfs(start):
        q = deque([start])
        visited[start] = True
        count = 1
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    count += 1
        return count

    for city in range(1, n + 1):
        if not visited[city]:
            component_size = bfs(city)
            total_cost += c_lib + (component_size - 1) * c_road

    return total_cost
