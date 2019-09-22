from collections import deque


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        graph, indegrees = {}, {}

        for i in range(numCourses):
            graph[i] = []
            indegrees[i] = 0

        # 初始化图
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
            indegrees[edge[1]] += 1

        queue = deque([])

        # 初始化 Queue
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != numCourses:
            return []

        order.reverse()
        return order
