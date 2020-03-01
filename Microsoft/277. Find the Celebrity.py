# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def knows(a, b):
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0

        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i

        for i in range(n):
            if i != celebrity and knows(celebrity, i):
                return -1
            if i != celebrity and not knows(i, celebrity):
                return -1

        return celebrity
