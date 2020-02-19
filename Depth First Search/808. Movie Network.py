from collections import deque
from heapq import heappush
from heapq import heappop

class Solution:
    """
    @param rating: the rating of the movies
    @param G: the realtionship of movies
    @param S: the begin movie
    @param K: top K rating
    @return: the top k largest rating moive which contact with S
    """
    def topKMovie(self, rating, G, S, K):
        visited = {S}
        queue = deque([S])
        connected = []

        while queue:
            node = queue.popleft()

            if node != S:
                heappush(connected, (-rating[node], node))

            for next_movie in G[node]:
                if next_movie not in visited:
                    visited.add(next_movie)
                    queue.append(next_movie)

        results = []
        i = 0
        while connected and i < K:
            _, movie = heappop(connected)
            results.append(movie)
            i += 1
        return results
