class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return a boolean, denote whether the array can be divided into k non-empty subsets whose sums are all equal
    """
    def partitiontoEqualSumSubsets(self, nums, k):
        target, reminder = divmod(sum(nums), k)

        if reminder != 0:
            return False

        nums = sorted(nums)

        if nums[-1] > target:
            return False

        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return self.search(nums, [0 for _ in range(k)], target)

    def search(self, nums, groups, target):
        if not nums:
            return True

        value = nums.pop()
        for i, group in enumerate(groups):
            if group + value <= target:
                groups[i] += value
                if self.search(nums, groups, target):
                    return True
                groups[i] -= value
            if not group:
                break
        nums.append(value)
        return False
