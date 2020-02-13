class Solution:
    """
    @param X: a integer
    @param Y: a integer
    @param nums: a list of integer
    @return: return the maximum index of largest prefix
    """
    def LongestPrefix(self, X, Y, nums):
        store = {X: 0, Y: 0}
        index = -1
        found = False
        for i in range(len(nums)):
            if nums[i] in store:
                store[nums[i]] += 1

            if store[X] == store[Y]:
                if store[X] != 0 and store[Y] != 0:
                    found = True
                index = i

        if not found:
            return -1
        return index
