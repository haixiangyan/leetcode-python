class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        self.results = []
        temp = []

        self.dfs(n, k, 1, 0, temp)

        return self.results

    def dfs(self, n, k, number, index, temp):
        if k == index:
            self.results.append(temp[:])

        for i in range(number, n + 1):
            temp.append(i)
            self.dfs(n, k, i + 1, index + 1, temp)
            temp.pop()
