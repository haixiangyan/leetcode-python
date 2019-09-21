from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def hasPath(self, maze, start, destination):
        if not maze:
            return False
        queue = deque([(start[0], start[1])])
        visited = {(start[0], start[1])}
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                if x == destination[0] and y == destination[1]:
                    return True

                for dx, dy in dirs:
                    nextX = x + dx
                    nextY = y + dy
                    while self.isValid(maze, nextX, nextY):
                        nextX += dx
                        nextY += dy
                    nextX -= dx
                    nextY -= dy
                    if (nextX, nextY) not in visited:
                        queue.append((nextX, nextY))
                        visited.add((nextX, nextY))

        return False

    def isValid(self, maze, x, y):
        rows, cols = len(maze), len(maze[0])
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 1
