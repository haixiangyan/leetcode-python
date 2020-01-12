from collections import deque

class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return rooms

        rows, cols = len(rooms), len(rooms[0])

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)

        return rooms

    def bfs(self, rooms, x, y):
        queue = deque([(x, y)])
        distance = 0

        while queue:
            distance += 1

            for _ in range(len(queue)):
                x, y = queue.popleft()

                for delta in range(4):
                    next_x, next_y = x + self.dx[delta], y + self.dy[delta]
                    if self.is_valid(rooms, next_x, next_y) and rooms[next_x][next_y] > distance:
                        queue.append((next_x, next_y))
                        rooms[next_x][next_y] = distance


    def is_valid(self, rooms, next_x, next_y):
        rows, cols = len(rooms), len(rooms[0])
        return 0 <= next_x < rows and 0 <= next_y < cols and rooms[next_x][next_y] != -1 and rooms[next_x][next_y] != 0
