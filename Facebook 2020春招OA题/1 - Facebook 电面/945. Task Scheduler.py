class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        c = [0 for _ in range(26)]
        for task in tasks:
            c[ord(task) - ord('A')] += 1

        c = sorted(c)

        i = 25
        while i >= 0 and c[25] == c[i]:
            i -= 1

        return max(len(tasks), (c[25] - 1) * (n + 1) + 25 - i)
