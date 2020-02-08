class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        indegrees = {node: 0 for node in graph}

        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1

        order = []
        for node in graph:
            if indegrees[node] == 0:
                self.dfs(node, indegrees, order)
        return order

    def dfs(self, node, indegrees, order):
        order.append(node)
        indegrees[node] -= 1

        for neighbor in node.neighbors:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                self.dfs(neighbor, indegrees, order)
