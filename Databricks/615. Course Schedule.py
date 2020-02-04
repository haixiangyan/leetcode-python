from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        indegrees = {}

        for i in range(numCourses):
            graph[i] = []
            indegrees[i] = 0

        for edge in prerequisites:
            child, parent = edge

            graph[parent].append(child)

            indegrees[child] += 1

        queue = deque([node for node in graph if indegrees[node] == 0])

        counts = 0
        while queue:
            node = queue.popleft()
            counts += 1
            for child in graph[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        return counts == numCourses
