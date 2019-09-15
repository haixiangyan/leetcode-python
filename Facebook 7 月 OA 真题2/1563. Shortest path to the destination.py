from collections import deque

class Solution:
    def __init__(self):
        self.DX = [1, 0, -1, 0]
        self.DY = [0, -1, 0, 1]
        self.visited = {'0-0'}
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        length = -1
        queue = deque([[0, 0]])

        while queue:
            len_queue = len(queue)
            length += 1
            for i in range(len_queue):
                print('1')
                point = queue.popleft()
                x, y = point[0], point[1]

                if targetMap[x][y] == 2:
                    return length

                if targetMap[x][y] == 1:
                    continue

                if targetMap[x][y] == 0:
                    for delta in range(4):
                        next_x = x + self.DX[delta]
                        next_y = y + self.DY[delta]
                        if self.is_valid(targetMap, next_x, next_y):
                            self.visited.add('' + str(next_x) + '-' + str(next_y))
                            queue.append([next_x, next_y])

        return 0

    def is_valid(self, targetMap, x, y):
        row, col = len(targetMap), len(targetMap[0])
        str_x_y = '' + str(x) + '-' + str(y)

        return (0 <= x < row) and (0 <= y < col) and (str_x_y not in self.visited)
