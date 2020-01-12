class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        while num >= 10:
            num = self.get_next_num(num)

        return num

    def get_next_num(self, num):
        next_num = 0

        while num != 0:
            next_num += num % 10

            num = num // 10

        return next_num
