class Solution:
    def reverseWords(self, s) -> None:
        self.reverse(s, 0, len(s) - 1)

        self.reverse_each_word(s)

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverse_each_word(self, s):
        n = len(s)

        start = end = 0
        while start < n:
            while end < n and s[end] != ' ':
                end += 1

            self.reverse(s, start, end - 1)

            start = end + 1
            end += 1
