class MyQueue:

    def __init__(self):
        self.forward = []
        self.backward = []

    def push(self, x: int) -> None:
        self.forward.append(x)

    def pop(self) -> int:
        result = -1
        if self.forward:
            self.switch(self.forward, self.backward)
            result = self.backward.pop()
            self.switch(self.backward, self.forward)
        return result

    def peek(self) -> int:
        if self.forward:
            return self.forward[0]
        else:
            return -1

    def empty(self) -> bool:
        return len(self.forward) == 0

    def switch(self, stack1, stack2):
        while stack1:
            stack2.append(stack1.pop())
