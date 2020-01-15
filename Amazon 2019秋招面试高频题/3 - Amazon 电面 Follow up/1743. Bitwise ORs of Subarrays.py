class Solution:
    """
    @param A: array A of non-negative integers.
    @return: Return the number of possible results.
    """
    def subarrayBitwiseORs(self, A):
        if not A:
            return 0

        result_set = set()
        curt_result_sets = [set() for _ in range(len(A))]

        result_set.add(A[-1])
        curt_result_sets[-1].add(A[-1])

        for i in range(len(A) - 2, -1, -1):
            result_set.add(A[i])
            curt_result_sets[i].add(A[i])

            for num in curt_result_sets[i + 1]:
                temp = num | A[i]
                result_set.add(temp)
                curt_result_sets[i].add(temp)

        return len(result_set)
