from collections import defaultdict
def common_courses(input, a, b):
    graph = defaultdict(set)
    for edge in input:
        id, course = edge
        graph[id].add(course)

    results = []
    for course in graph[a]:
        if course in graph[b]:
            results.append(course)
    return results


input = [(1, 'cs'), (2, 'math'), (3, 'math'), (3, 'econ'), (1, 'jaaa'), (3, 'dog'), (4, 'cat'), (5, 'dog')]
print(common_courses(input, 5, 3))