class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def __init__(self):
        self.graph = {}
        self.results = []
        self.lowerbound = {}

    def get_next_words(self, word, dictonary):
        next_words = []

        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word in dictonary and next_word != word:
                    next_words.append(next_word)

        return next_words

    def findLadders(self, start, end, dictonary):
        dictonary.add(start)
        dictonary.add(end)

        limit = 0

        for word in dictonary:
            self.graph[word] = self.get_next_words(word, dictonary)
            self.lowerbound[word] = self.get_diff(word, end)

        while len(self.results) == 0:
            self.dfs(limit, 1, start, end, [start])
            limit += 1

        return self.results

    def get_diff(self, a, b):
        diffs = 0

        for i in range(len(a)):
            if a[i] != b[i]:
                diffs += 1

        return diffs

    def dfs(self, limit, index, word, end, path):
        if index > limit:
            if word == end:
                self.results.append(path[:])
            return

        if index - 1 + self.lowerbound[word] > limit:
            return

        for next_word in self.graph[word]:
            path.append(next_word)
            self.dfs(limit, index + 1, next_word, end, path)
            path.pop()

        if len(self.results) == 0:
            self.lowerbound[word] = max(self.lowerbound[word], limit - (index - 1) + 1)
