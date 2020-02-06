class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        m, n = len(a), len(b)
        i, j = m - 1, n - 1

        result = ''
        carrier, remain = 0, 0

        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            curt = x + y + carrier
            carrier = curt // 2
            remain = curt % 2

            i -= 1
            j -= 1

            result = str(remain) + result

        if carrier == 1:
            result = str(carrier) + result

        return result
