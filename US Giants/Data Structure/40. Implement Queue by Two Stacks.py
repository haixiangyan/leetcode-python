class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def ajust(self):
        if len(self.stack2) != 0:
            return

        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

    def push(self, element):
        self.stack1.append(element)


    def pop(self):
        self.ajust()
        return self.stack2.pop()

    def top(self):
        self.ajust()
        return self.stack2[len(self.stack2) - 1]