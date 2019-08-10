class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
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

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, permutation, visited, length)
            permutation.pop()
            visited[i] = False
