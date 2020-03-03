class Solution:
    def __init__(self):
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def findWords(self, board, words):
        if not board or not board[0]:
            return []

        word_set, prefix_set = set(words), set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                first = board[i][j]
                self.search(board, i, j, board[i][j], word_set, prefix_set, {(i, j)}, result)

        return list(result)

    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return

        if word in word_set:
            result.add(word)

        for delta_x, delta_y in self.directions:
            next_x, next_y = x + delta_x, y + delta_y

            if not self.inside(board, next_x, next_y):
                continue
            if (next_x, next_y) in visited:
                continue

            visited.add((next_x, next_y))
            self.search(board, next_x, next_y, word + board[next_x][next_y], word_set, prefix_set, visited, result)
            visited.remove((next_x, next_y))

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
