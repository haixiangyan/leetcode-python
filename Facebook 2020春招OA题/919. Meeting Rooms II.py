class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        points = []

        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        ongoing_meetings = 0
        rooms = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            rooms = max(rooms, ongoing_meetings)

        return rooms
