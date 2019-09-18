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
            distance = self.getDistance(origin, point)

            heapq.heappush(heap, (-distance, -point.x, -point.y))

            if len(heap) > k:
                heapq.heappop(heap)

        results = []
        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            results.append(Point(-x, -y))

        results.reverse()
        return results


    def getDistance(self, origin, target):
        return pow(target.x - origin.x, 2) + pow(target.y - origin.y, 2)
