from collections import deque
class MyStack:

    def __init__(self):
        self.queuein = deque()
    def push(self, x: int) -> None:
        self.queuein.append(x)
    def pop(self) -> int:
        for i in range(len(self.queuein) - 1):
            self.queuein.append(self.queuein.popleft())
        return self.queuein.popleft()
    def top(self) -> int:
        x = self.pop()
        self.queuein.append(x)
        return x
    def empty(self) -> bool:
        return len(self.queuein) == 0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()