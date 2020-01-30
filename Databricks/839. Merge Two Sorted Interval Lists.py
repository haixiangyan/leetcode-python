class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        results = []
        n, m = len(list1), len(list2)
        i, j = 0, 0

        for _ in range(n + m):
            if i < n and (j >= m or list1[i].start < list2[j].start):
                self.push_back(results, list1[i])
                i += 1
            else:
                self.push_back(results, list2[j])
                j += 1

        return results

    def push_back(self, results, interval):
        if not results:
            results.append(interval)
            return

        last = results[-1]
        if last.end < interval.start:
            results.append(interval)
            return

        last.end = max(last.end, interval.end)
