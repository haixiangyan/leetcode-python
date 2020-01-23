from collections import deque


class Solution:
    def longestStrChain(self, words):
        words = sorted(words, key=len)
        word_dict = set(words)
        longest = 0
        memo = {}

        for word in words:
            longest = max(longest, self.bfs(word, word_dict, memo))

        return longest

    def bfs(self, word, word_dict, memo):
        length, longest = 0, 0
        queue = deque([word])

        while queue:
            length += 1

            for _ in range(len(queue)):
                word = queue.popleft()
                for next_word in self.get_next_words(word, word_dict):
                    if next_word in memo:
                        longest = max(longest, length + memo[next_word])
                    else:
                        queue.append(next_word)

        memo[word] = max(longest, length)
        return memo[word]

    def get_next_words(self, word, word_dict):
        next_words = []
        for i in range(len(word)):
            next_word = word[:i] + word[i + 1:]
            if next_word in word_dict:
                next_words.append(next_word)
        return next_words
