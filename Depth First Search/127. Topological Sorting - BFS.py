from collections import deque

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

        queue = deque([node for node in graph if indegrees[node] == 0])
        order = []
        while queue:
            curt = queue.popleft()
            order.append(curt)

            for neighbor in curt.neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return order
