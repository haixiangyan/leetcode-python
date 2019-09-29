class NestedInteger(object):
    def isInteger(self):
        pass

    def getInteger(self):
        pass

    def getList(self):
        pass


class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        self.nextElement = None

        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        if self.nextElement is None:
            self.hasNext()

        curtNextElement, self.nextElement = self.nextElement, None
        return curtNextElement

    def hasNext(self):
        if self.nextElement is not None:
            return True

        while self.stack:
            top = self.stack.pop()

            if top.isInteger():
                self.nextElement = top.getInteger()
                return True

            for item in reversed(top.getList()):
                self.stack.append(item)

        return False
