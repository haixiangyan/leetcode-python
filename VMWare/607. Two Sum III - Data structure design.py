class TwoSum:
    def __init__(self):
        self.cache = {}
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        if number not in self.cache:
            self.cache[number] = 0
        self.cache[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num in self.cache:
            # value = 2 * num
            if value - num == num and self.cache[num] > 1:
                return True
            # value != 2 * num
            if value - num != num and value - num in self.cache:
                return True
        return False
