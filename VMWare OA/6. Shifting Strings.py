class Solution:
    def getShiftedString(self, str, left_shifts, right_shifts):
        if not str:
            return str

        length = len(str)

        # Get relative shifts
        shifts = (left_shifts - right_shifts) % length

        if shifts == 0:
            return str

        # Shift left
        if shifts > 0:
            return str[shifts:] + str[:shifts]
        # Shift right
        else:
            return str[length - shifts:] + str[:length - shifts]

s = Solution()
str = 'abcde'
left_shifts = 4
right_shifts = 2
print(s.getShiftedString(str, left_shifts, right_shifts))
