from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        queue = deque([beginWord])
        visited = {beginWord}
        wordList = set(wordList)

        steps = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return steps

                for next_word in self.get_next_words(word, wordList, visited):
                    queue.append(next_word)
                    visited.add(next_word)
            steps += 1

        return 0

    def get_next_words(self, word, wordList, visited):
        next_words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue
                next_word = word[:i] + char + word[i + 1:]
                if next_word not in visited and next_word in wordList:
                    next_words.append(next_word)
        return next_words
