class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def addOperators(self, nums, target):
        results = []

        self.dfs(nums, 0, 0, 0, '', target, results, len(nums))

        return results

    def dfs(self, nums, index, last, curt, path, target, results, n):
        if index == n:
            if curt == target:
                results.append(path[:])
            return

        for i in range(index, n):
            x = int(nums[index:i + 1])
            if index == 0:
                self.dfs(nums, i + 1, x, x, str(x), target, results, n)
            else:
                self.dfs(nums, i + 1, x, curt + x, path + '+' + str(x), target, results, n)
                self.dfs(nums, i + 1, -x, curt - x, path + '-' + str(x), target, results, n)
                self.dfs(nums, i + 1, last * x, curt - last + last * x, path + '*' + str(x), target, results, n)

            if x == 0:
                break
