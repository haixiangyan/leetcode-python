class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        n = len(graph)
        colors = [0 for _ in range(n)]

        for i in range(n):
            if colors[i] == 0 and not self.draw(i, colors, graph, 1):
                return False
        return True

    def draw(self, node, colors, graph, color):
        colors[node] = color

        for next_node in graph[node]:
            if colors[next_node] == 0 and not self.draw(next_node, colors, graph, -color):
                return False
            if colors[next_node] == colors[node]:
                return False
        return True
