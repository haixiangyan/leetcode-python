class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        pairs = [(num, i) for i, num in enumerate(nums)]
        pairs = sorted(pairs, key=lambda x: x[0])
        target = abs(target)
        n = len(pairs)

        for i in range(n):
            j = i + 1
            while j < n:
                diff = pairs[j][0] - pairs[i][0]

                if diff < target:
                    j += 1
                elif diff > target:
                    break
                else:
                    return [
                        min(pairs[i][1] + 1, pairs[j][1] + 1),
                        max(pairs[i][1] + 1, pairs[j][1] + 1)
                    ]

        return [-1, -1]
