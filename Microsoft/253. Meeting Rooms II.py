class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0

        points = []
        for interval in intervals:
            points.append((interval[0], 1))
            points.append((interval[1], -1))

        meeting, rooms = 0, 0
        for _, delta in sorted(points):
            meeting += delta
            rooms = max(rooms, meeting)

        return rooms
