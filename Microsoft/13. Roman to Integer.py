class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = ROMAN[s[-1]]
        for index in range(len(s) - 2, -1, -1):
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                result -= ROMAN[s[index]]
            else:
                result += ROMAN[s[index]]
        return result
