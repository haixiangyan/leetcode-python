class Solution:
    def isBipartite(self, graph) -> bool:
        self.colors = [0 for _ in range(len(graph))]

        for i in range(len(graph)):
            if self.colors[i] == 0 and not self.mark(i, graph, 1):
                return False
        return True

    def mark(self, curt, graph, color):
        self.colors[curt] = color
        for child in graph[curt]:
            if self.colors[child] == 0 and not self.mark(child, graph, -color):
                return False
            elif self.colors[child] == self.colors[curt]:
                return False
        return True
