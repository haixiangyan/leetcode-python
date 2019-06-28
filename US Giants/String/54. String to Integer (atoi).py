import sys

class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # MaxInt
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        str = str.strip()

        if str == '':
            return 0

        index = 0
        sign = 1
        result = 0

        # Get number sign
        if str[index] == '-':
            sign = -1
            index += 1
        if str[index] == '+':
            sign = 1
            index += 1

        while index < len(str):
            if str[index] < '0' or str[index] > '9':
                break

            result = result * 10 + int(str[index])

            if result > sys.maxsize:
                return MAX_INT

            index += 1

        result = sign * result

        if result >= MAX_INT:
            return MAX_INT
        if result <= MIN_INT:
            return MIN_INT

        return result
