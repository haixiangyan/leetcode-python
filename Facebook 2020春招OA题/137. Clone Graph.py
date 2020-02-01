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
        root = node
        if node is None:
            return node

        nodes = self.get_nodes(node)

        store = {}

        for node in nodes:
            store[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            new_node = store[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(store[neighbor])

        return store[root]

    def get_nodes(self, node):
        queue = deque([node])
        visited = {node}

        while queue:
            curt = queue.popleft()
            for neighbor in curt.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return list(visited)
