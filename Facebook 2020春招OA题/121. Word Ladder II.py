from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)

        distances = {}

        self.bfs(end, distances, dict)

        results = []
        self.dfs(distances, start, [start], end, results, dict)

        return results

    def bfs(self, end, distances, dict):
        queue = deque([end])
        distances[end] = 0
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                for next_word in self.get_next_words(word, dict):
                    if next_word not in distances:
                        distances[next_word] = distances[word] + 1
                        queue.append(next_word)

    def get_next_words(self, word, dict):
        next_words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i + 1:]
                if next_word in dict:
                    next_words.append(next_word)
        return next_words

    def dfs(self, distances, curt, path, end, results, dict):
        if curt == end:
            results.append(path[:])
            return

        for next_word in self.get_next_words(curt, dict):
            if distances[next_word] == distances[curt] - 1:
                path.append(next_word)
                self.dfs(distances, next_word, path, end, results, dict)
                path.pop()
