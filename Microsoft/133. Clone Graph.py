from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        root = node
        graph = self.get_graph(node)

        mapping = {}
        for node in graph:
            mapping[node] = Node(node.val)

        for node in graph:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor])

        return mapping[root]

    def get_graph(self, node):
        graph = {node}
        queue = deque([node])

        while queue:
            curt = queue.popleft()
            for neighbor in curt.neighbors:
                if neighbor not in graph:
                    graph.add(neighbor)
                    queue.append(neighbor)
        return graph
