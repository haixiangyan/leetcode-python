import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.positions = {}
        self.length = 0

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        if val in self.positions:
            return False

        self.nums.append(val)
        self.positions[val] = self.length

        self.length += 1

        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        if val not in self.positions:
            return False

        index, last= self.positions[val], self.nums[-1]
        self.nums[index] = last
        self.positions[last] = index

        # Remove all info
        self.nums.pop()
        del self.positions[val]

        self.length -= 1

        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        return self.nums[random.randint(0, self.length - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()