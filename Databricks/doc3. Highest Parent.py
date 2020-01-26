# 1     2  3
# /  \  /      \
# 4    5        6
#                   \
#                    7
# 输入是int[][] input, input[0]是input[1] 的parent，比如 {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}会形成上面的图

class Solution:
    def __init__(self):
        self.result = None
        self.steps = 0

    def highest_parent(self, edges, node):
        graph = self.get_graph(edges)
        self.dfs(graph, node, 0)
        return self.result

    def dfs(self, graph, node, curt_steps):
        parents = graph[node]

        if curt_steps > self.steps:
            self.steps = curt_steps
            self.result = node

        if parents:
            for parent in parents:
                self.dfs(graph, parent, curt_steps + 1)

    def get_graph(self, edges):
        graph = {}

        for edge in edges:
            parent, node = edge

            if node not in graph:
                graph[node] = []
            graph[node].append(parent)
            if parent not in graph:
                graph[parent] = []

        return graph

s = Solution()
edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
node = 7
print(s.highest_parent(edges, node))
