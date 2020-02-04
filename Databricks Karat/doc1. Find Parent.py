# Time complexity: O(n)
# Space complexity: O(n)
def find_parent(edges):
    graph = {}
    for edge in edges:
        parent, child = edge

        if child not in graph:
            graph[child] = set()
        if parent not in graph:
            graph[parent] = set()

        graph[child].add(parent)

    return [node for node in graph if len(graph[node]) <= 1]

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(find_parent(edges))
