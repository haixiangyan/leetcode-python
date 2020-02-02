from heapq import heapify
from heapq import heappush
from heapq import heappop

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        graph = self.build_graph(words)
        return self.top_order(graph)

    def build_graph(self, words):
        graph = {}

        for word in words:
            for char in word:
                graph[char] = set()

        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break

        return graph

    def top_order(self, graph):
        indegrees = {node: 0 for node in graph}


        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        order = ''
        queue = [node for node in graph if indegrees[node] == 0]
        heapify(queue)

        while queue:
            node = heappop(queue)
            order += node

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heappush(queue, neighbor)

        if len(order) != len(graph):
            return ''
        return order
