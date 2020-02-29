class Solution:
    def addStrings(self, num1, num2):
        carrier = 0
        digits = ""
        i = 0
        num1Len = len(num1)
        num2Len = len(num2)
        maxLen = max(num1Len, num2Len)
        while i < maxLen:
            theSum = carrier
            if i < num1Len:
                theSum += int(num1[num1Len - 1 - i])
            if i < num2Len:
                theSum += int(num2[num2Len - 1 - i])
            carrier = theSum // 10
            theSum = theSum % 10
            digits = str(theSum) + digits

            i += 1
        if carrier == 1:
            return "1" + digits

        return digits
