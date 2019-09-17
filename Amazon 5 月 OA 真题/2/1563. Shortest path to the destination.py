from collections import deque


class Solution:
    def __init__(self):
        self.DX = [1, 0, -1, 0]
        self.DY = [0, 1, 0, -1]
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        if not targetMap:
            return -1

        queue = deque([(0, 0)])
        visited = {(0, 0)}
        length = -1

        while queue:
            queueLength = len(queue)
            length += 1

            for _ in range(queueLength):
                (x, y) = queue.popleft()

                if targetMap[x][y] == 2:
                    return length

                for delta in range(4):
                    nextX, nextY = x + self.DX[delta], y + self.DY[delta]

                    if self.isValid(targetMap, nextX, nextY) and (nextX, nextY) not in visited:
                        queue.append((nextX, nextY))
                        visited.add((nextX, nextY))

        return -1

    def isValid(self, targetMap, x, y):
        rows, cols = len(targetMap), len(targetMap[0])
        return 0 <= x < rows and 0 <= y < cols and targetMap[x][y] != 1
