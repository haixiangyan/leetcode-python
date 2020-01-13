class Direction:
    UP = 'UP'
    DOWN = 'DOWN'


class Status:
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'


class Request:
    def __init__(self, l=0):
        self.level = l

    def getLevel(self):
        return self.level


class ElevatorButton:
    def __init__(self, level, e):
        self.level = level
        self.elevator = e

    def pressButton(self):
        request = InternalRequest(self.level)
        self.elevator.handleInternalRequest(request)


class ExternalRequest(Request):
    def __init__(self, l=0, d=None):
        Request.__init__(self, l)
        self.direction = d

    def getDirection(self):
        return self.direction


class InternalRequest(Request):
    def __init__(self, l=None):
        Request.__init__(self, l)


class Elevator:
    def __init__(self, n):
        # Keep them, don't modify.
        self.buttons = []
        self.upStops = []
        self.downStops = []
        for i in range(n):
            self.upStops.append(False)
            self.downStops.append(False)
        self.currLevel = 0
        self.status = Status.IDLE

    def insertButton(self, eb):
        self.buttons.append(eb)

    # 1. 设置去往的楼层
    # 2. 根据 request 的方向 -> 改变电梯方向
    def handleExternalRequest(self, r):
        if r.getDirection() == Direction.UP:
            self.upStops[r.getLevel() - 1] = True
            if self.noRequests(self.downStops):
                self.status = Status.UP
        else:
            self.downStops[r.getLevel() - 1] = True
            if self.noRequests(self.upStops):
                self.status = Status.DOWN

    # 1. 改变去往的楼层
    # 2. 只能去同方向的楼层
    def handleInternalRequest(self, r):
        if self.status == Status.UP:
            if r.getLevel() >= self.currLevel + 1:
                self.upStops[r.getLevel() - 1] = True
        elif self.status == Status.DOWN:
            if r.getLevel() <= self.currLevel + 1:
                self.downStops[r.getLevel() - 1] = True

    # 1. 根据方向 -> 去所有同方向的楼层
    def openGate(self):
        if self.status == Status.UP:
            for i in range(len(self.upStops)):
                # 尝试最靠近 currLevel 的楼层
                checkLevel = (self.currLevel + i) % len(self.upStops)
                if self.upStops[checkLevel]:
                    self.currLevel = checkLevel
                    self.upStops[checkLevel] = False
                    break

        elif self.status == Status.DOWN:
            for i in range(len(self.downStops)):
                # 尝试离 currLevel 最远的楼层
                checkLevel = (self.currLevel + len(self.downStops) - i) % len(self.downStops)
                if self.downStops[checkLevel]:
                    self.currLevel = checkLevel
                    self.downStops[checkLevel] = False
                    break

    def closeGate(self):
        if self.status == Status.IDLE:
            if self.noRequests(self.downStops):
                self.status = Status.UP
                return
            if self.noRequests(self.upStops):
                self.status = Status.DOWN
        elif self.status == Status.UP:
            if self.noRequests(self.upStops):
                if self.noRequests(self.downStops):
                    self.status = Status.IDLE
                else:
                    self.status = Status.DOWN
        elif self.status == Status.DOWN:
            if self.noRequests(self.downStops):
                if self.noRequests(self.upStops):
                    self.status = Status.IDLE
                else:
                    self.status = Status.UP

    def noRequests(self, stops):
        for stop in stops:
            if stop:
                return False
        return True

    def elevatorStatusDescription(self):
        description = "Currently elevator status is : " + self.status + \
                      ".\nCurrent level is at: " + str(self.currLevel + 1) + \
                      ".\nup stop list looks like: " + self.toString(self.upStops) + \
                      ".\ndown stop list looks like:  " + self.toString(self.downStops) + \
                      ".\n*****************************************\n"
        return description

    @classmethod
    def toString(cls, stops):
        return str(stops).replace("False", "false").replace("True", "true")