class NestedInteger(object):
    def isInteger(self):
        pass
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        pass
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        pass
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer


class NestedIterator(object):

    def __init__(self, nestedList):
        self.nextElement = None
        self.stack = []

        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        if self.nextElement is None:
            self.hasNext()
        curtNext, self.nextElement = self.nextElement, None
        return curtNext

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
