from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        if node is None:
            return None

        graph = self.build_graph(node)

        mapping = {}
        for old_node in graph:
            mapping[old_node] = UndirectedGraphNode(old_node.label)

        for old_node in graph:
            new_node = mapping[old_node]
            for neighbor in graph[old_node]:
                new_node.neighbors.append(mapping[neighbor])

        return mapping[node]

    def build_graph(self, node):
        graph = {}
        queue = deque([node])
        visited = {node}
        while queue:
            curt = queue.popleft()
            if curt not in graph:
                graph[curt] = []

            for neighbor in curt.neighbors:
                graph[curt].append(neighbor)

                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return graph
