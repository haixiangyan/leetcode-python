from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        indegrees = {node: 0 for node in range(numCourses)}
        graph = {node: [] for node in range(numCourses)}

        for child, parent in prerequisites:
            graph[parent].append(child)
            indegrees[child] += 1

        queue = deque([node for node in indegrees if indegrees[node] == 0])
        visited = set(queue)
        while queue:
            node = queue.popleft()

            for child in graph[node]:
                if child not in visited:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        queue.append(child)
                        visited.add(child)

        return len(visited) == numCourses
