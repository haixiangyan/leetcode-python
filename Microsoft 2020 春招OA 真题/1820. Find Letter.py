class Solution:
    """
    @param str: the str
    @return: the letter
    """
    def findLetter(self, str):
        lower = set()
        upper = set()

        for char in str:
            if 'a' <= char <= 'z':
                lower.add(char)
            if 'A' <= char <= 'Z':
                upper.add(char)

        result = '~'
        for char in upper:
            if char.lower() not in lower:
                continue

            if result == '~' or ord(char) > ord(result):
                result = char
        return result
