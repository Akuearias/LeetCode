# https://leetcode.cn/problems/course-schedule-ii/solutions/249149/ke-cheng-biao-ii-by-leetcode-solution
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        nodes = set()
        for p in prerequisites:
            graph[p[1]].append(p[0])
            nodes.add(p[0])
            nodes.add(p[1])

        visited = [0] * numCourses
        S = []
        B = True

        def DFS(i):
            nonlocal B
            visited[i] = 1
            for nb in graph[i]:
                if visited[nb] == 0:
                    DFS(nb)
                    if not B:
                        return
                elif visited[nb] == 1:
                    B = False
                    return

            visited[i] = 2
            S.append(i)

        for i in range(numCourses):
            if B and not visited[i]:
                DFS(i)

        if not B:
            return []

        return S[::-1]