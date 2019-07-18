class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        A = list(A)

        while k > 0:
            has_deleted = False
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    del A[i]
                    has_deleted = True
                    break

            if not has_deleted and len(A) > 1:
                A.pop()

            k -= 1

        while len(A) > 0 and A[0] == '0':
            del A[0]

        return ''.join(A)
