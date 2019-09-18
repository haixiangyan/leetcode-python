from collections import deque

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def __init__(self):
        self.DX = [1, 1, -1, -1, 2, 2, -2, -2]
        self.DY = [2, -2, 2, -2, 1, -1, 1, -1]
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        if not grid:
            return -1

        queue = deque([source])
        visited = {(source.x, source.y)}
        length = -1

        while queue:
            queueLength = len(queue)
            length += 1

            for _ in range(queueLength):
                point = queue.popleft()

                if point.x == destination.x and point.y == destination.y:
                    return length

                for delta in range(8):
                    nextPoint = Point(point.x + self.DX[delta], point.y + self.DY[delta])

                    if self.isValid(nextPoint, grid) and (nextPoint.x, nextPoint.y) not in visited:
                        queue.append(nextPoint)
                        visited.add((nextPoint.x, nextPoint.y))

        return -1


    def isValid(self, point, grid):
        rows, cols = len(grid), len(grid[0])
        return 0 <= point.x < rows and 0 <= point.y < cols and grid[point.x][point.y] != 1
