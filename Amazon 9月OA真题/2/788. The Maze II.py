from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        queue = deque([(start[0], start[1], 0)])
        visited = {(start[0], start[1])}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minDist = -1

        while queue:
            size = len(queue)

            for _ in range(size):
                x, y, front = queue.popleft()

                if x == destination[0] and y == destination[1]:
                    minDist = front if minDist == -1 else min(minDist, front)

                for dx, dy in directions:
                    nextX, nextY = x + dx, y + dy
                    count = 0
                    while self.isValid(maze, nextX, nextY):
                        nextX += dx
                        nextY += dy
                        count += 1
                    nextX -= dx
                    nextY -= dy

                    if (nextX, nextY) not in visited:
                        queue.append((nextX, nextY, front + count))
                        visited.add((nextX, nextY))

        return minDist

    def isValid(self, maze, x, y):
        rows, cols = len(maze), len(maze[0])
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
