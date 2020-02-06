from collections import deque
def multi_course_path(edges):
    graph = {}
    indegrees = {}

    for edge in edges:
        parent, child = edge

        if parent not in graph:
            graph[parent] = []
        if child not in graph:
            graph[child] = []
        graph[parent].append(child)

        indegrees[parent] = indegrees.get(parent, 0) + 0
        indegrees[child] = indegrees.get(child, 0) + 1

    queue = deque([course for course in graph if indegrees[course] == 0])
    order = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        order.append(level)

    return order[len(graph) // 2 - 1]

input = [('course1', 'course2'), ('course3', 'course4'), ('course2', 'course3'), ('course4', 'course5')]
print(multi_course_path(input))
