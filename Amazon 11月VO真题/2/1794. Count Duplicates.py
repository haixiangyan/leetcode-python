class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def CountDuplicates(self, nums):
        counts = {}
        results = []

        for number in nums:
            if number not in counts:
                counts[number] = 1
            else:
                if counts[number] == 1:
                    results.append(number)
                counts[number] += 1

        return results
