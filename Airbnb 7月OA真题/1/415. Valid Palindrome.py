class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        cleanupString = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                cleanupString += char.lower()

        n = len(cleanupString)
        left = n // 2 - 1
        right = left + (1 if n % 2 == 0 else 2)

        while 0 <= left and right < n:
            if cleanupString[left] != cleanupString[right]:
                return False
            left -= 1
            right += 1
        return True
