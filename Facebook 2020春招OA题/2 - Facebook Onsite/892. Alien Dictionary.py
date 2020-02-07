from collections import deque
from heapq import heapify
from heapq import heappop
from heapq import heappush


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        indegrees = {}
        graph = {}

        # 初始化
        for word in words:
            for char in word:
                graph[char] = []
                indegrees[char] = 0

        # 构图
        for i in range(1, len(words)):
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i - 1][j] == words[i][j]:
                    continue
                graph[words[i - 1][j]].append(words[i][j])
                indegrees[words[i][j]] += 1
                break

        # 初始化 queue
        queue = [char for char in graph if indegrees[char] == 0]
        heapify(queue)

        order = []

        while queue:
            for _ in range(len(queue)):
                curt = heappop(queue)
                order.append(curt)

                for next_char in graph[curt]:
                    indegrees[next_char] -= 1
                    if indegrees[next_char] == 0:
                        heappush(queue, next_char)

        if len(order) != len(graph):
            return ''

        return ''.join(order)
