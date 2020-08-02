class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            cur_sum = n1 + n2 + carry

            carry = cur_sum // 10

            result = str(cur_sum % 10) + result

            i, j = i - 1, j - 1

        return result
