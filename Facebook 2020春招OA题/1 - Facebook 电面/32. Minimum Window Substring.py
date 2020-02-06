class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        target_hash = self.get_target_hash(target)
        n = len(source)
        min_len = n
        start, end = 0, 0
        j = 0

        matched_char, target_char = 0, len(target_hash)
        window = {}

        for i in range(n):
            while j < n and matched_char < target_char:
                char = source[j]

                if char in target_hash:
                    window[char] = window.get(char, 0) + 1
                    if window[char] == target_hash[char]:
                        matched_char += 1
                j += 1

            if j - i < min_len and matched_char == target_char:
                min_len = j - i
                start, end = i, j

            char = source[i]
            if char in target_hash:
                if window[char] == target_hash[char]:
                    matched_char -= 1
                window[char] -= 1
        return source[start:end]

    def get_target_hash(self, target):
        store = {}
        for char in target:
            store[char] = store.get(char, 0) + 1
        return store
