class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x:x.start)
        results = []
        left, right = intervals[0].start, intervals[0].end
        for interval in intervals:
            if right < interval.start:
                results.append(Interval(left, right))
                left, right = interval.start, interval.end
                continue

            right = max(right, interval.end)

        results.append(Interval(left, right))

        return results
