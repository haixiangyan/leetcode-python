from math import sqrt

class Solution:
    """
    @param num: the given number
    @return: whether whether there're two integers
    """
    def checkSumOfSquareNumbers(self, num):
        if num < 0:
            return False

        upperbound = int(sqrt(num))
        if upperbound ** 2 == num:
            return True

        for i in range(1, upperbound + 1):
            j = int(sqrt(num - i * i))

            if i * i + j * j == num:
                return True

        return False
