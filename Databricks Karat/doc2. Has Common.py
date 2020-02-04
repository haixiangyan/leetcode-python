def has_common(edges, a, b):
    graph = get_graph(edges)

    a_parents = {a}
    b_parents = {b}

    get_parents(graph, a, a_parents)
    get_parents(graph, b, b_parents)

    for parent in a_parents:
        if parent in b_parents:
            return True

    return False

def get_parents(graph, node, parents):
    if node not in graph:
        return

    for parent in graph[node]:
        parents.add(parent)

def get_graph(edges):
    graph = {}

    for edge in edges:
        parent, child = edge

        if parent not in graph:
            graph[parent] = set()
        if child not in graph:
            graph[child] = set()

        graph[child].add(parent)

    return graph

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(has_common(edges, 4, 5))
