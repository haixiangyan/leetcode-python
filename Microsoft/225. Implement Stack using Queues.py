from collections import deque

class MyStack:

    def __init__(self):
        self.main = deque([])
        self.support = deque([])

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        while len(self.main) > 1:
            self.support.append(self.main.popleft())

        result = self.main.pop()

        self.support, self.main = self.main, self.support

        return result

    def top(self) -> int:
        while len(self.main) > 1:
            self.support.append(self.main.popleft())

        result = self.main.pop()

        self.support.append(result)
        self.support, self.main = self.main, self.support

        return result

    def empty(self) -> bool:
        return len(self.main) == 0
