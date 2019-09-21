import collections
from collections import deque
class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def numBusesToDestination(self, routes, S, T):
        if not routes:
            return -1

        stopToBus = collections.defaultdict(list)

        # 该站对应是第几个 route
        for index, route in enumerate(routes):
            for stop in route:
                stopToBus[stop].append(index)

        queue = deque([S])
        visitedStop = {S}
        visitedBus = set()
        distance = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                stop = queue.popleft()
                for bus in stopToBus[stop]:
                    if bus not in visitedBus:
                        visitedBus.add(bus)
                        for nextStop in routes[bus]:
                            if nextStop == T:
                                return distance
                            if nextStop not in visitedStop:
                                queue.append(nextStop)
                                visitedStop.add(nextStop)

            distance += 1
        return -1
