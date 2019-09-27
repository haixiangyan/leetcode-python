from heapq import heapify
from heapq import heappop
from heapq import heappush


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

        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()

        for i in range(1, len(words)):
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i - 1][j] != words[i][j]:
                    graph[words[i - 1][j]].add(words[i][j])
                    break

        return graph


    def topOrder(self, graph):
        indegree = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        heap = [node for node in graph if indegree[node] == 0]
        heapify(heap)

        results = ''
        while heap:
            node = heappop(heap)
            results += node

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(heap, neighbor)

        return results if len(results) == len(graph) else ''
