def course_path(input):
    graph = {}
    indegrees = {}
    for edge in input:
        parent, child = edge
        if parent not in graph:
            graph[parent] = None
        if child not in graph:
            graph[child] = None
        graph[parent] = child

        if child not in indegrees:
            indegrees[child] = 0
        if parent not in indegrees:
            indegrees[parent] = 0
        indegrees[child] += 1

    n = len(graph)

    start = None
    for course in graph:
        if indegrees[course] == 0:
            start = course

    for i in range(n // 2 - 1):
        start = graph[start]
    return start

input = [('course1', 'course2'), ('course3', 'course4'), ('course2', 'course3'), ('course4', 'course5')]
print(course_path(input))