class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, x):
        self.stack.append(x)

        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(self.max_stack[-1], x))

    """
    @return: An integer
    """

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """

    def top(self):
        return self.stack[-1]

    """
    @return: An integer
    """

    def peekMax(self):
        return self.max_stack[-1]

    """
    @return: An integer
    """

    def popMax(self):
        target = self.max_stack[-1]

        buffer = []
        while self.stack[-1] != target:
            buffer.append(self.stack.pop())

        self.stack.pop()

        while buffer:
            self.stack.append(buffer.pop())
        return target
