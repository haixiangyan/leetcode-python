class Solution:
    """
    @param points: a set of points
    @return: the min area
    """

    def minimumAreaRectangle(self, points):
        result = float('inf')
        points = sorted(points, key=lambda point: (point[1], point[0]))
        n = len(points)

        for i in range(n):
            q = i + 1
            while q < n:
                if points[q][0] != points[i][0]:
                    q += 1
                    continue
                height1 = points[q][1] - points[i][1]
                if height1 == 0:
                    continue

                for k in range(i + 1, n):
                    if points[k][1] != points[i][1]:
                        break
                    width = points[k][0] - points[i][0]
                    if width == 0:
                        continue

                    j = k + 1
                    while j < n:
                        if points[j][0] != points[k][0]:
                            j += 1
                            continue
                        height2 = points[j][1] - points[k][1]
                        if height2 == 0 or height1 != height2:
                            j += 1
                            continue

                        result = min(result, height1 * width)
                        break
                q += 1
        if result == float('inf'):
            return 0
        else:
            return result
