class MinStack:

    def __init__(self):
        self.stack = []
        self.__min = [float('inf')]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.__min[-1]:
            self.__min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.__min[-1]:
            self.__min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.__min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()