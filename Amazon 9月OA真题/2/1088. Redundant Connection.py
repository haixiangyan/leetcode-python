class UnionFind:
    def __init__(self, n):
        self.fathers = {}

        for i in range(1, n + 1):
            self.fathers[i] = i

    def find(self, node):
        path = []
        while self.fathers[node] != node:
            node = self.fathers[node]
            path.append(node)

        for n in path:
            self.fathers[n] = node

        return node

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def connect(self, a, b):
        self.fathers[self.find(a)] = self.find(b)

class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """
    def findRedundantConnection(self, edges):
        if not edges:
            return None
        uf = UnionFind(len(edges))

        for first, second in edges:
            if uf.query(first, second):
                return first, second
            else:
                uf.connect(first, second)

        return None
