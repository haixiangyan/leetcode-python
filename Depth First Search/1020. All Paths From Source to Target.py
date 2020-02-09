class Solution:
    """
    @param graph: a 2D array
    @return: all possible paths from node 0 to node N-1
    """

    def allPathsSourceTarget(self, graph):
        paths = []

        self.dfs(graph, 0, len(graph) - 1, [0], paths)

        return paths

    def dfs(self, graph, node, target, path, paths):
        if node == target:
            paths.append(path[:])
            return

        for next_node in graph[node]:
            path.append(next_node)
            self.dfs(graph, next_node, target, path, paths)
            path.pop()
