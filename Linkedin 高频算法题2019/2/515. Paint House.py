class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        r, b, g = 0, 0, 0

        for r_c, b_c, g_c in costs:
            r, b, g = r_c + min(b, g), b_c + min(r, g), g_c + min(r, b)

        return min(r, b, g)
