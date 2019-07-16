class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        xor = a ^ b

        count = 0
        for i in range(32):
            if xor & (1 << i) != 0:
                count += 1

        return count
