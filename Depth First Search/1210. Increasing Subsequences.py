class Solution:
    """
    @param nums: an integer array
    @return: all the different possible increasing subsequences of the given array
    """
    def findSubsequences(self, nums):
        sequences = []

        self.dfs(nums, 0, [], sequences)

        return sequences

    def dfs(self, nums, index, curt, sequences):
        if index <= len(nums) and len(curt) >= 2:
            sequences.append(curt[:])

        visited = {}

        for i in range(index, len(nums)):
            if curt and curt[-1] > nums[i]:
                continue

            if nums[i] in visited:
                continue

            visited[nums[i]] = True

            curt.append(nums[i])
            self.dfs(nums, i + 1, curt, sequences)
            curt.pop()
