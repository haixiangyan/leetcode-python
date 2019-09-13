class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)

        if len(self.min_stack) == 0:
            self.min_stack.append(number)
        else:
            # 存储当时状态下的最小值
            self.min_stack.append(min(number, self.min_stack[-1]))

    """
    @return: An integer
    """
    def pop(self):
        poping_element = self.stack[-1]
        del(self.stack[-1], self.min_stack[-1])
        return poping_element

    """
    @return: An integer
    """
    def min(self):
        return self.min_stack[-1]