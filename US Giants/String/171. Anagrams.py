class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        if strs is None:
            return []

        dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in dict:
                dict[sorted_word] = [word]
            else:
                dict[sorted_word] += [word]

        results = []

        for sorted_word in dict:
            if len(dict[sorted_word]) >= 2:
                results += dict[sorted_word]

        return results
