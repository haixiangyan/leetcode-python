class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return len(s) != len(nums)
