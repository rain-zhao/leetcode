class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
param_1 = obj.deleteHead()
obj.appendTail(5)
obj.appendTail(2)
param_2 = obj.deleteHead()
param_3 = obj.deleteHead()

print(param_1)
print(param_2)
print(param_3)
