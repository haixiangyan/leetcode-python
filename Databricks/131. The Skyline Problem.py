# Lintcode: https://www.lintcode.com/problem/the-skyline-problem/description
class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        points = self.get_skyline(buildings)

        return self.get_ranges(points)

    def get_skyline(self, buildings):
        n = len(buildings)

        if n == 0:
            return []

        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        left_skyline = self.get_skyline(buildings[:n // 2])
        right_skyline = self.get_skyline(buildings[n // 2:])

        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left_skyline, right_skyline):
        left = right = 0
        left_len, right_len = len(left_skyline), len(right_skyline)
        current_y = left_y = right_y = 0

        skyline = []

        while left < left_len and right < right_len:
            left_point, right_point = left_skyline[left], right_skyline[right]

            if left_point[0] < right_point[0]:
                x, left_y = left_point
                left += 1
            else:
                x, right_y = right_point
                right += 1

            max_y = max(left_y, right_y)

            if max_y != current_y:
                self.update_skyline(x, max_y, skyline)
                current_y = max_y

        self.append_skyline(left_skyline, left, left_len, current_y, skyline)
        self.append_skyline(right_skyline, right, right_len, current_y, skyline)

        return skyline

    def update_skyline(self, x, y, skyline):
        if not skyline or skyline[-1][0] != x:
            skyline.append([x, y])
        else:
            skyline[-1][1] = y

    def append_skyline(self, rest_skyline, start, length, current_y, skyline):
        for i in range(start, length):
            x, y = rest_skyline[i]
            if y != current_y:
                self.update_skyline(x, y, skyline)
                current_y = y

    def get_ranges(self, points):
        ranges = []

        for i in range(len(points) - 1):
            x_start, y = points[i]
            x_end, _ = points[i + 1]
            if y == 0:
                continue
            ranges.append([x_start, x_end, y])
        return ranges