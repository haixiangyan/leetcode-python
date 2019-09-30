class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        if not str:
            return ''

        store = {}

        for char in str:
            if char not in store:
                store[char] = 0
            store[char] += 1

        for char in store:
            if store[char] == 1:
                return char

        return ''
