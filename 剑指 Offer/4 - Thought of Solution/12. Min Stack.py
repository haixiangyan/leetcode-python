class MinStack:
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, number):
        if self.minStack:
            self.minStack.append(min(number, self.minStack[-1]))
        else:
            self.minStack.append(number)
        self.stack.append(number)

    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def min(self):
        return self.minStack[-1]
