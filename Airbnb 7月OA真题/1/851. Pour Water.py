class Solution:
    """
    @param heights: the height of the terrain
    @param V: the units of water
    @param K: the index
    @return: how much water is at each index
    """
    def pourWater(self, heights, V, K):
        n = len(heights)
        for _ in range(V):
            position = K
            for i in range(K + 1, n):
                if heights[i - 1] > heights[i]:
                    position = i
                elif heights[i - 1] < heights[i]:
                    break
            for i in range(K - 1, -1, -1):
                if heights[i] < heights[i + 1]:
                    position = i
                elif heights[i] > heights[i + 1]:
                    break
            heights[position] += 1
        return heights
