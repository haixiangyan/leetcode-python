class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        first, second = 0, 1

        for i in range(n - 1):
            first, second = second, first + second

        return first
