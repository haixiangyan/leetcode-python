class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        
        self.father = {i: i for i in range(n)}
        self.size = n
        for a, b in edges:
            self.union(a, b)
        
        return self.size == 1
    
    def union(self, a, b):
        fatherA = self.find(a)
        fatherB = self.find(b)

        if fatherA != fatherB:
            self.size -= 1
            self.father[fatherA] = fatherB
    
    def find(self, node):
        path = []

        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        
        for n in path:
            self.father[n] = node

        return node