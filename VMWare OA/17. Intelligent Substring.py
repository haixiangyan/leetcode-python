class Solution:
    def encode(self, char, values):
        return 1 if values[ord(char) - ord('a')] == '0' else 0

    def getSpecialSubstring(self, str, k, values):
        if not str:
            return 0

        left, counts, max_len = 0, 0, 0
        for right in range(len(str)):
            counts += self.encode(str[right], values)

            if counts > k:
                while self.encode(str[left], values) == 0:
                    counts -= 1
                    left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
