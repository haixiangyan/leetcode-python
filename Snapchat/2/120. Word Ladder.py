from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = deque([start])
        visited = {start}
        distance = 0

        while queue:
            size = len(queue)
            distance += 1

            for i in range(size):
                word = queue.popleft()

                if word == end:
                    return distance

                for nextWord in self.getNextWords(word):
                    if nextWord not in dict or nextWord in visited:
                        continue
                    queue.append(nextWord)
                    visited.add(nextWord)

        return -1

    def getNextWords(self, word):
        nextWords = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstunwxyz':
                nextWords.append(left + char + right)
        return nextWords
