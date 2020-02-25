class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        results = []
        for interval in intervals:
            if not results:
                results.append(interval)
                continue
            if results[-1][1] < interval[0]:
                results.append(interval)
                continue
            results[-1][1] = max(results[-1][1], interval[1])

        return results
