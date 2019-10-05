class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def push(self, element):
        self.firstStack.append(element)

    def pop(self):
        if not self.secondStack:
            self.switch()
        return self.secondStack.pop()

    def top(self):
        if not self.secondStack:
            self.switch()
        return self.secondStack[-1]

    def switch(self):
        while self.firstStack:
            self.secondStack.append(self.firstStack.pop())
