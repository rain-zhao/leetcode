class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minVal = min(self.minVal, x) if self.minVal else x

    def pop(self) -> None:
        val = self.stack.pop()
        # 简单实现
        if val == self.minVal:
            self.minVal = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.getMin()
obj.pop()
param_2 = obj.top()
param_3 = obj.getMin()
