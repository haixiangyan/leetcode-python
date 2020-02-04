import heapq
class Solution:
    """
    @param courses: duration and close day of each course
    @return: the maximal number of courses that can be taken
    """
    def scheduleCourse(self, courses):
        # 按 deadline 排好序
        courses = sorted(courses, key=lambda x: x[1])

        curt_time = 0
        heap = []
        for duration, deadline in courses:
            curt_time += duration
            heapq.heappush(heap, -duration)

            if curt_time > deadline:
                # 去掉之前一个最大的 duration
                curt_time -= (-heapq.heappop(heap))

        return len(heap)
