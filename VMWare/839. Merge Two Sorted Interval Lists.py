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
        intervals = []
        i1, i2 = 0, 0
        m, n = len(list1), len(list2)

        while i1 < m and i2 < n:
            if list1[i1].start < list2[i2].start:
                self.push_back(intervals, list1[i1])
                i1 += 1
            else:
                self.push_back(intervals, list2[i2])
                i2 += 1

        while i1 < m:
            self.push_back(intervals, list1[i1])
            i1 += 1
        while i2 < n:
            self.push_back(intervals, list2[i2])
            i2 += 1

        return intervals

    def push_back(self, intervals, curt):
        if not intervals:
            intervals.append(curt)
            return

        last = intervals[-1]

        if last.end < curt.start:
            intervals.append(curt)
            return

        last.end = max(last.end, curt.end)
