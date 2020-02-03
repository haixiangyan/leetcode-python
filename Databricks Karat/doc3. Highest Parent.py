class Solution:
    def __init__(self):
        self.result = None

    def highest_parent(self, edges, node):
        if not edges:
            return self.result

        graph = self.get_graph(edges)

        self.dfs(graph, node)

        return self.result

    def dfs(self, graph, node):
        self.result = node
        for parent in graph[node]:
            self.dfs(graph, parent)

    def get_graph(self, edges):
        graph = {}

        for edge in edges:
            parent, child = edge
            if child not in graph:
                graph[child] = []
            graph[child].append(parent)
            if parent not in graph:
                graph[parent] = []
        return graph

s = Solution()
edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
node = 7
print(s.highest_parent(edges, node))
