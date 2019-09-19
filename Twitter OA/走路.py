from collections import deque

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def solution(start, end):
    visited = {(start.x, start.y)}
    queue = deque([start])

    while queue and len(visited) < 100 * 100:
        size = len(queue)
        for _ in range(size):
            point = queue.popleft()

            if point.x == end.x and point.y == end.y:
                return True

            # (x, x + y)
            nextPoint = Point(point.x, point.x + point.y)
            if isValid(nextPoint) and (nextPoint.x, nextPoint.y) not in visited:
                queue.append(nextPoint)
                visited.add((nextPoint.x, nextPoint.y))

            nextPoint = Point(point.x + point.y, point.y)
            if isValid(nextPoint) and (nextPoint.x, nextPoint.y) not in visited:
                queue.append(nextPoint)
                visited.add((nextPoint.x, nextPoint.y))

    return False

def isValid(nextPoint):
    return 0 <= nextPoint.x < 100 and 0 <= nextPoint.y < 100


start = Point(1, 2)
end = Point(2, 1)
print(solution(start, end))
