import heapq

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        heap = []

        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(heap, (dist, point.x, point.y))

        results = []
        for i in range(k):
            _, x, y= heapq.heappop(heap)
            results.append(Point(x, y))

        return results

    def getDistance(self, a, b):
        return pow(b.x - a.x, 2) + pow(b.y - a.y, 2)
