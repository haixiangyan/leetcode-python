class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if n <= 0:
            return False

        return n & (n - 1) == 0
