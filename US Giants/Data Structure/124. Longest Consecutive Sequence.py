class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        num_set = set()
        longest = 0

        for i in range(len(num)):
            num_set.add(num[i])

        for i in range(len(num)):
            down = num[i] - 1

            while down in num_set:
                num_set.remove(down)
                down -= 1

            up = num[i] + 1

            while up in num_set:
                num_set.remove(up)
                up += 1

            longest = max(longest, up - down - 1)

        return longest
