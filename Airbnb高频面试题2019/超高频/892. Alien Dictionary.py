import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = self.buildGraph(words)
        return self.topOrder(graph)

    def buildGraph(self, words):
        graph = {}
        n = len(words)

        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()

        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break

        return graph

    def topOrder(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        queue = [node for node in graph if indegrees[node] == 0]
        heapq.heapify(queue)

        order = ''
        while queue:
            node = heapq.heappop(queue)
            order += node
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heapq.heappush(queue, neighbor)

        return order if len(order) == len(graph) else ''
