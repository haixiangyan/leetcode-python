class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0

        while n != 0:
            count += n / 5
            n /= 5

        return count
