class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        self.results = []
        permutation = []
        nums = sorted(nums)
        length = len(nums)
        visited = [False for i in range(length)]

        self.dfs(nums, permutation, visited, length)

        return self.results

    def dfs(self, nums, permutation, visited, length):
        if len(permutation) == length:
            self.results.append(permutation[:])
            return

        for i in range(length):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, permutation, visited, length)
            permutation.pop()
            visited[i] = False
