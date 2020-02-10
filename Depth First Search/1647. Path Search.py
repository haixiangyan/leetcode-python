class Solution:
    """
    @param n: The number of points
    @param G: The description of graph
    @param S: The point S
    @param T: The point T
    @return: output all the paths from S to T
    """
    def getPath(self, n, G, S, T):
        graph = {node: [] for node in range(n)}
        for edge in G:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        for node in graph:
            graph[node].sort()

        visited = [False for _ in range(n)]
        visited[S] = True
        paths = []
        self.dfs(S, T, graph, [S], paths, visited)
        return paths

    def dfs(self, curt, end, graph, path, paths, visited):
        if curt == end:
            paths.append(path[:])
            return

        for next_node in graph[curt]:
            if visited[next_node]:
                continue

            visited[next_node] = True
            path.append(next_node)
            self.dfs(next_node, end, graph, path, paths, visited)
            path.pop()
            visited[next_node] = False
