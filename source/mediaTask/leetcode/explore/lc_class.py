class MinStack:
    """最小栈"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        elif self.min[-1] > x:
            self.min.append(x)

    def pop(self) -> None:
        slen = len(self.stack)
        n = self.stack.pop(slen - 1)
        if n not in self.stack:
            if n in self.min:
                self.min.remove(n)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
