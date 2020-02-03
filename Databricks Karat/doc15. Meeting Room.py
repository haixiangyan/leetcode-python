class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True

        timeline = []
        for interval in intervals:
            timeline.append((interval.start, 1))
            timeline.append((interval.end, -1))

        ongoing_meeting = 0
        rooms = 0
        for item in sorted(timeline):
            ongoing_meeting += item[1]
            rooms = max(rooms, ongoing_meeting)

        return rooms == 1
