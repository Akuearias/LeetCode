import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        nodes = set()
        for p in prerequisites:
            graph[p[1]].append(p[0])
            nodes.add(p[0])
            nodes.add(p[1])

        visited = [False] * numCourses
        onPath = [False] * numCourses
        self.dummy = False

        def DFS(curr):
            if onPath[curr]:
                self.dummy = True
                return

            if visited[curr] or self.dummy:
                return

            visited[curr] = True
            onPath[curr] = True
            for nb in graph[curr]:
                DFS(nb)
            onPath[curr] = False

        for i in range(numCourses):
            if not visited[i]:
                DFS(i)
                if self.dummy:
                    return False

        return True