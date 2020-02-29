class MovingAverage:

    def __init__(self, size: int):
        self.window = []
        self.total = 0
        self.num = 0
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)
        self.total += val
        self.num += 1

        if self.num <= self.size:
            return self.total / self.num
        else:
            first = self.window.pop(0)
            self.total -= first
            return self.total / self.size
