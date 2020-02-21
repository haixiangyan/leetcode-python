class Solution:
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        word = ''
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                word = self.get_small(num % 1000) + self.thousands[i] + ' ' + word
            num = num // 1000
        return word.strip()

    def get_small(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.lessThan20[num] + ' '
        elif num < 100:
            return self.tens[num // 10] + ' ' + self.get_small(num % 10)
        else:
            return self.lessThan20[num // 100] + ' Hundred ' + self.get_small(num % 100)
