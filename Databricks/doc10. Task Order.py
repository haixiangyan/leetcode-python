from collections import deque

# 算task和pretask輸出task by level的那題. Just calculate indegree, bfs
# 是像這樣
# input = {
# {"cook", "eat"},   // do "cook" before "eat"
# {"study", "eat"},
# {"sleep", "study"}}
#
# output (steps of a workflow):
# {{"sleep", "cook"},.
# {"study"},
# {"eat"}}
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

        queue = deque([])
        counts = 0
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            counts += 1
            for next_node in graph[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)

        return counts == numCourses
