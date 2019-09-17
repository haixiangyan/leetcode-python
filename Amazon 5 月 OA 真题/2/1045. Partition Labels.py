class Solution:
    def __init__(self):
        self.store = {}
        self.results = []

    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """

    def partitionLabels(self, S):
        results = []
        right, left = 0, 0
        mostRight = {char: index for index, char in enumerate(S)}

        for index, char in enumerate(S):
            right = max(right, mostRight[char])

            if index == right:
                results.append(index - left + 1)
                left = index + 1

        return results
