class Solution:
    def min_times(self, bags):
        if not bags:
            return 0

        bags = sorted(bags)
        left, right = 0, len(bags) - 1
        count = 0

        while left <= right:
            curt_sum = bags[left] + bags[right]

            if curt_sum > 3:
                count += 1
                right -= 1
            else:
                left += 1
                right -= 1
                count += 1
        return count

s = Solution()
bags = [1.01, 1.01, 1.99, 2.5]
print(s.min_times(bags))
