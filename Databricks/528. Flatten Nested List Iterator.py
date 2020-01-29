class NestedIterator(object):

    def __init__(self, nested_list):
        self.stack = []
        self.nested_list = nested_list
        self.next_elem = None

        for item in reversed(nested_list):
            self.stack.append(item)

    # @return {int} the next element in the iteration
    def next(self):
        if self.next_elem is None:
            self.hasNext()

        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        if self.next_elem:
            return True

        while self.stack:
            if self.stack[-1].isInteger():
                self.next_elem = self.stack.pop().getInteger()
                return True
            else:
                for item in reversed(self.stack.pop().getList()):
                    self.stack.append(item)

        return False
