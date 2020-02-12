# Leetcode: https://leetcode.com/problems/the-skyline-problem/
class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def getSkyline(self, buildings):
        n = len(buildings)

        # Base case
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            # 左上和右下
            return [[x_start, y], [x_end, 0]]

        left_skyline = self.getSkyline(buildings[:n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])

        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left_skyline, right_skyline):
        left_len, right_len = len(left_skyline), len(right_skyline)
        left = right = 0
        current_y = left_y = right_y = 0
        skylines = []

        # 合并共有的部分
        while left < left_len and right < right_len:
            left_point, right_point = left_skyline[left], right_skyline[right]
            # 选择第一个点
            if left_point[0] < right_point[0]:
                x, left_y = left_point
                left += 1
            else:
                x, right_y = right_point
                right += 1

            # 合并楼层的高
            max_y = max(left_y, right_y)
            # 如果 y 值要变，要更新 skyline 了
            if max_y != current_y:
                self.update_skyline(x, max_y, skylines)
                current_y = max_y

        # 将剩下的部分加入到 skyline
        self.append_skyline(left, left_len, left_skyline, current_y, skylines)
        self.append_skyline(right, right_len, right_skyline, current_y, skylines)

        return skylines

    def update_skyline(self, x, y, skylines):
        # 没有这个点的时候就加入
        if not skylines or skylines[-1][0] != x:
            skylines.append([x, y])
        # 否则更新最后一个点的 y 值
        else:
            skylines[-1][1] = y

    def append_skyline(self, index, length, rest_skyline, current_y, skylines):
        while index < length:
            x, y = rest_skyline[index]
            index += 1
            # 如果 y 值要变，要更新 skyline 了
            if current_y != y:
                self.update_skyline(x, y, skylines)
                current_y = y
