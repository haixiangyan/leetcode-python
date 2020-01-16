class Solution:
    def min_times(self, bags):
        if not bags:
            return 0

        bags = sorted(bags)
        counts = 0
        i = 0
        n = len(bags)

        while i < n:
            total = 0
            j = i

            while j < n and total + bags[j] < 3:
                total += bags[j]
                j += 1

            counts += 1
            i = j

        return counts

s = Solution()
bags = [1.01, 1.01, 1.99, 2.5]
print(s.min_times(bags))
