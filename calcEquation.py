from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        S = [float(-1) for _ in range(len(queries))]

        nodes = set()
        for equation in equations:
            for node in equation:
                nodes.add(node)

        graph = {}
        for i, equation in enumerate(equations):
            graph[(equation[0], equation[1])] = values[i]
            graph[(equation[1], equation[0])] = 1 / values[i]

        def DFS(x, y, visited):
            if (x, y) in graph:
                return graph[(x, y)]
            visited.add(x)

            for n in nodes:
                if (x, n) in graph and n not in visited:
                    value = DFS(n, y, visited)
                    if value != float(-1):
                        return graph[(x, n)] * value

            return float(-1)

        for i, (x, y) in enumerate(queries):
            if x in nodes and y in nodes:
                S[i] = DFS(x, y, set())

        return S

