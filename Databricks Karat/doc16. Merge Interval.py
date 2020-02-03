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
        results = []

        intervals = sorted(intervals, key=lambda x: x.start)

        for interval in intervals:
            if not results:
                results.append(interval)
                continue

            last = results[-1]
            if last.end < interval.start:
                results.append(interval)
                continue

            last.end = max(last.end, interval.end)

        return results
