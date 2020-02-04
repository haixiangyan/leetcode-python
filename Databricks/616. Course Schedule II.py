from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        graph = {node: [] for node in range(numCourses)}
        indegrees = [0 for _ in range(numCourses)]

        for edge in prerequisites:
            child, parent = edge
            graph[parent].append(child)
            indegrees[child] += 1

        order = []
        queue = deque([node for node in graph if indegrees[node] == 0])

        while queue:
            node = queue.popleft()
            order.append(node)

            for child in graph[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        if len(order) != numCourses:
            return []
        return order
