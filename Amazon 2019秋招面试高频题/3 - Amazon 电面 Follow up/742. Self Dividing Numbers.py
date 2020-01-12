class Solution:
    """
    @param lower: Integer : lower bound
    @param upper: Integer : upper bound
    @return: a list of every possible Digit Divide Numbers
    """

    def digitDivideNums(self, lower, upper):
        if lower > upper:
            return []

        results = []

        for num in range(lower, upper + 1):
            if self.is_dividable(num):
                results.append(num)

        return results

    def is_dividable(self, num):
        original = num
        while num != 0:
            digit = num % 10

            if digit == 0 or original % digit != 0:
                return False

            num = num // 10

        return True