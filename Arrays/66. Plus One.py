from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        carrier = 1

        for i in range(len(digits) - 1, -1, -1):
            if carrier == 0:
                break

            carrier, digits[i] = divmod(digits[i] + carrier, 10)

        if carrier == 1:
            digits = [1] + digits

        return digits
