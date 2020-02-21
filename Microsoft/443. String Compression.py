class Solution:
    def compress(self, chars) -> int:
        left, i = 0, 0

        while i < len(chars):
            char, length = chars[i], 1

            while i + 1 < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1

            chars[left] = char

            if length > 1:
                len_str = str(length)
                chars[left + 1: left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1

        return left
