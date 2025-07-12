import collections


# I don't know why not all test cases are passed.
# Link: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs
class Graph:
    def __init__(self, n):
        self.nodes = n
        self.connections = collections.defaultdict(set)

    def connect(self, x, y):
        if x != y:
            self.connections[x].add(y)
            self.connections[y].add(x)

    def find_all_distances(self, s):
        if s not in self.connections:
            return

        queue = collections.deque([s])
        visited = set([s])
        distances = [-1] * self.nodes
        distances[s] = 0

        while queue:
            current = queue.popleft()
            for neighbor in self.connections[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distances[neighbor] = distances[current] + 6
                    queue.append(neighbor)

        for i in range(self.nodes):
            if i != s:
                print(distances[i], end=' ')
        print()


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
