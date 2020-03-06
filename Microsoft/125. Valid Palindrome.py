class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''
        for char in s:
            if char.isdigit() or char.isalpha():
                clean_str += char.lower()

        n = len(clean_str)
        left = n // 2 - 1
        right = left + (1 if n % 2 == 0 else 2)

        while 0 <= left and right < n:
            if clean_str[left] != clean_str[right]:
                return False
            left -= 1
            right += 1
        return True
