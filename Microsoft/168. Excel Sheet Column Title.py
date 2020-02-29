class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''

        while n > 0:
            n -= 1
            result = chr(n % 26 + ord('A')) + result
            n = n // 26

        return result
