class Solution(object):
    def twoSum(self, nums, target):
        store = {}

        for i, num in enumerate(nums):
            if target - num in store:
                return [store[target - num], i]
            store[num] = i

        return [-1, -1]
