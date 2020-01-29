class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.matrix = vec2d
        self.row = 0
        self.col = -1
        self.next_elem = None
        self.rows = len(self.matrix)

    # @return {int} a next element
    def next(self):
        if self.next_elem is None:
            self.hasNext()

        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        if self.next_elem:
            return True

        self.col += 1
        while self.row < self.rows and self.col >= len(self.matrix[self.row]):
            self.row += 1
            self.col = 0

        if self.row < self.rows and self.col < len(self.matrix[self.row]):
            self.next_elem = self.matrix[self.row][self.col]
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())