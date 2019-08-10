class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        indegrees = {}

        # 初始化入度为 0
        for node in graph:
            indegrees[node] = 0

        # 更新相邻节点入度
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1

        results = []

        # 递归更新节点
        for node in graph:
            if indegrees[node] == 0:
                self.dfs(node, indegrees, results)

        return results

    def dfs(self, node, indegrees, results):
        results.append(node)
        indegrees[node] -= 1

        # 所有相邻节点的入度都要减 1
        for neighbor in node.neighbors:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                self.dfs(neighbor, indegrees, results)