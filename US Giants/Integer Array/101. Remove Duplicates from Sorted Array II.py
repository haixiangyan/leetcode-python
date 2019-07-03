class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        result = []

        before = None
        count = 0

        for number in nums:
            if number != before:
                result.append(number)
                before = number
                count = 1
            elif count < 2:
                result.append(number)
                count += 1

        for i, number in enumerate(result):
            nums[i] = result[i]

        return len(result)
