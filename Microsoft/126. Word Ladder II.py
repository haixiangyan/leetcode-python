from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        wordList.add(beginWord)

        distance = {}

        self.bfs(endWord, distance, wordList)

        results = []
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)

        return results

    def bfs(self, start, distance, wordList):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, wordList):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, wordList):
        next_words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i + 1:]
                if next_word != word and next_word in wordList:
                    next_words.append(next_word)
        return next_words

    def dfs(self, curt, target, distance, wordList, path, results):
        if curt == target:
            results.append(path[:])
            return

        for word in self.get_next_words(curt, wordList):
            if distance[word] != distance[curt] - 1:
                continue

            path.append(word)
            self.dfs(word, target, distance, wordList, path, results)
            path.pop()
