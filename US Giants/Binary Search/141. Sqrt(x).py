class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        low, high = 0, x

        while low + 1 < high:
            root = (low + high) // 2

            if root < x // root:
                low = root
            else:
                high = root

        if high * high <= x:
            return high
        else:
            return low
