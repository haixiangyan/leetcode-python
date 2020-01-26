# 1     2  3
# /  \  /      \
# 4    5        6
#                   \
#                    7
# 输入是int[][] input, input[0]是input[1] 的parent，比如 {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}会形成上面的图

# 第二问是 两个指定的点有没有公共祖先
def has_common(edges, a, b):
    graph = get_graph(edges)

    a_parents = set()
    b_parents = set()

    get_parents(graph, a, a_parents)
    get_parents(graph, b, b_parents)

    for parent in a_parents:
        if parent in b_parents:
            return True
    return False


def get_graph(edges):
    graph = {}

    for edge in edges:
        parent, node = edge

        if node not in graph:
            graph[node] = []
        graph[node].append(parent)
        if parent not in graph:
            graph[parent] = []

    return graph

def get_parents(graph, node, all_parents):
    curt_parents = graph[node]

    if not curt_parents:
        return

    for parent in curt_parents:
        all_parents.add(parent)
        get_parents(graph, parent, all_parents)

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(has_common(edges, 4, 5))
