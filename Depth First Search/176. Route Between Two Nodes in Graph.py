class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def __init__(self):
        self.visited = set()
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        if s == t:
            return True

        for next_node in s.neighbors:
            if next_node in self.visited:
                continue

            self.visited.add(s)

            if self.hasRoute(graph, next_node, t):
                return True
        return False
