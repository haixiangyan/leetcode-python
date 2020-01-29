import random
import collections

class RandomizedCollection(object):

    def __init__(self):
        self.nums = []
        self.positions = collections.defaultdict(set)
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.positions[val].add(self.length)

        self.length += 1

        return len(self.positions[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.positions[val]:
            return False

        index = self.positions[val].pop()
        self.nums[index] = None

        self.length -= 1

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        x = None
        while x is None:
            x = random.choice(self.nums)
        return x

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()