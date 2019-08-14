class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return None

        nodes = self.get_nodes(node)

        mapper = {}

        for original_node in nodes:
            mapper[original_node] = UndirectedGraphNode(original_node.label)

        for original_node in nodes:
            for original_neighbor in original_node.neighbors:
                mapper[original_node].neighbors.append(mapper[original_neighbor])

        return mapper[node]
    
    def get_nodes(self, node):
        queue = collections.deque([node])
        nodes = set([node])

        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in nodes:
                    nodes.add(neighbor)
                    queue.append(neighbor)

        return nodes