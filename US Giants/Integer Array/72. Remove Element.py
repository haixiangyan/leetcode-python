class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        result_length = 0

        for index in range(len(A)):
            if A[index] != elem:
                temp = A[index]
                A[index] = A[result_length]
                A[result_length] = temp

                result_length += 1

        return result_length
