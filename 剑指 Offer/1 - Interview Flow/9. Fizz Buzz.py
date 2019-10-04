class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('fizz buzz')
                continue
            if i % 3 == 0:
                results.append('fizz')
                continue
            if i % 5 == 0:
                results.append('buzz')
                continue
            if i % 3 != 0 and i % 5 != 0:
                results.append(str(i))
        return results
