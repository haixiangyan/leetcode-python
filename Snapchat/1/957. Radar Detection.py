class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param coordinates: The radars' coordinate
    @param radius: Detection radius of radars
    @return: The car was detected or not
    """
    def radarDetection(self, coordinates, radius):
        if not coordinates:
            return 'NO'

        for i in range(len(coordinates)):
            if abs(coordinates[i].y) <= radius[i]:
                return 'YES'

        return 'NO'
