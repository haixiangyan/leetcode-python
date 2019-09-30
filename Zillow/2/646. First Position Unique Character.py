class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        store = {}

        for char in s:
            if char not in store:
                store[char] = 0
            store[char] += 1
        
        for index, char in enumerate(s):
            if store[char] == 1:
                return index

        return -1
