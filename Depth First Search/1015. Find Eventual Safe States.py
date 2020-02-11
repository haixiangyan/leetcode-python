class Solution:
    """
    @param graph: a 2D integers array
    @return: return a list of integers
    """
    def eventualSafeNodes(self, graph):
        secure = set()
        visited = set()

        for node in range(len(graph)):
            visited.add(node)
            self.dfs(node, graph, secure, visited)
            visited.remove(node)

        return sorted(list(secure))

    def dfs(self, node, graph, secure, visited):
        for next_node in graph[node]:
            if next_node in secure:
                continue
            if next_node in visited:
                return False

            visited.add(next_node)
            is_secure = self.dfs(next_node, graph, secure, visited)
            visited.remove(next_node)
            if not is_secure:
                return False

        secure.add(node)
        return True
