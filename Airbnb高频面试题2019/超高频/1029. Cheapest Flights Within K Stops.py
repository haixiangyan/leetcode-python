class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        distance = [float('inf') for _ in range(n)]
        distance[src] = 0

        for step in range(K + 1):
            copyDistance = list(distance)
            for u, v, w in flights:
                copyDistance[v] = min(copyDistance[v], distance[u] + w)
            distance = copyDistance

        return distance[dst] if distance[dst] != float('inf') else -1
