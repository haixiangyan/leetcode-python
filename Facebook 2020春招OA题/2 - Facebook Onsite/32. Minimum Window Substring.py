from collections import Counter
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        window = {}
        target_dict = Counter(list(target))
        n = len(source)
        j = 0

        target_char, matched_char = len(target_dict), 0
        min_length = n + 1
        start, end = 0, 0

        for i in range(n):
            while j < n and matched_char < target_char:
                if source[j] in target_dict:
                    window[source[j]] = window.get(source[j], 0) + 1
                    if window[source[j]] == target_dict[source[j]]:
                        matched_char += 1
                j += 1

            if matched_char == target_char and j - i < min_length:
                min_length = j - i
                start, end = i, j

            if source[i] in target_dict:
                if window[source[i]] == target_dict[source[i]]:
                    matched_char -= 1
                window[source[i]] -= 1

        return source[start:end]
