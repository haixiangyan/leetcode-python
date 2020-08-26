class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        results = []
        if not nums:
            results.append(self.helper(lower, upper))
            return results
        
        pre_point = lower - 1

        for point in nums:
            if pre_point != point and pre_point + 1 != point:
                results.append(self.helper(pre_point + 1, point - 1))
            pre_point = point
        
        if nums[-1] < upper:
            results.append(self.helper(nums[-1] + 1, upper))

        return results

    
    def helper(self, lower, upper):
        if lower == upper:
            return str(lower)
        
        return str(lower) + '->' + str(upper)

