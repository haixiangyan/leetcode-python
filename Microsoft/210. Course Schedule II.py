from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        graph = {node: [] for node in range(numCourses)}
        indegrees = {node: 0 for node in range(numCourses)}

        for child, parent in prerequisites:
            graph[parent].append(child)
            indegrees[child] += 1

        queue = deque([node for node in graph if indegrees[node] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for child in graph[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        if len(order) == numCourses:
            return list(order)
        else:
            return []
