class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        store = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))

            if sorted_str not in store:
                store[sorted_str] = []
            store[sorted_str].append(str)

        return store.values()
