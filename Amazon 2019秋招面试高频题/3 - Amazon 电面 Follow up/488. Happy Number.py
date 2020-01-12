class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        store = set()

        while n != 1:
            if n in store:
                return False

            next_happy = self.get_next_happy(n)

            store.add(n)

            n = next_happy

        return True

    def get_next_happy(self, n):
        result = 0

        while n != 0:
            result += (n % 10) * (n % 10)

            n = n // 10

        return result
