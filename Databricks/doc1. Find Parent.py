# 1     2  3
# /  \  /      \
# 4    5        6
#                   \
#                    7
# 输入是int[][] input, input[0]是input[1] 的parent，比如 {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}会形成上面的图
# 第一问是只有0个parents和只有1个parent的节点
def find_parent(edges):
    indegrees = {}

    for edge in edges:
        parent, node = edge

        indegrees[node] = indegrees.get(node, 0) + 1
        indegrees[parent] = indegrees.get(parent, 0)

    results = []
    for node, indegree in indegrees.items():
        if indegree == 0 or indegree == 1:
            results.append(node)

    return results

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(find_parent(edges))
