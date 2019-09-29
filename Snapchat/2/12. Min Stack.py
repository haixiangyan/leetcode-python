class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, number):
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        else:
            self.minStack.append(min(number, self.minStack[-1]))

    def pop(self):
        result = self.stack[-1]
        del(self.stack[-1], self.minStack[-1])
        return result

    def min(self):
        return self.minStack[-1]
