class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)
    
    def pop(self) -> None:
        main = self.stack.pop()
        if main == self.minimum[-1]:
            self.minimum.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minimum[-1]























    # def __init__(self):
    #     self.stack = []
    #     self.minimum = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minimum or val <= self.minimum[-1]:
    #         self.minimum.append(val)
    
    # def pop(self) -> None:
    #     main = self.stack.pop()
    #     if main == self.minimum[-1]:
    #         self.minimum.pop()
    
    # def top(self) -> int:
    #     return self.stack[-1]
    
    # def getMin(self) -> int:
    #     return self.minimum[-1]

    # def __init__(self):
    #     self.stack = []
    #     self.minimum = []
    
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minimum or val <= self.minimum[-1]:
    #         self.minimum.append(val)

    # def pop(self) -> None:
    #     main = self.stack.pop()
    #     if main == self.minimum[-1]:
    #         self.minimum.pop()
        
    # def top(self) -> int:
    #     return self.stack[-1]
    
    # def getMin(self) -> int:
    #     return self.minimum[-1]


    # def __init__(self):
    #     self.stack = []
    #     self.minimum = []
    
    # def push(self, val):
    #     self.stack.append(val)
    #     if not self.minimum or val <= self.minimum[-1]:
    #         self.minimum.append(val)

    # def pop(self):
    #     main = self.stack.pop()
    #     if main == self.minimum[-1]:
    #         self.minimum.pop()
    
    # def top(self):
    #     return self.stack[-1]
    
    # def getMin(self):
    #     return self.minimum[-1]


    # def __init__(self):
    #     self.stack = []
    #     self.minimum = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minimum or val <= self.minimum[-1]:
    #         self.minimum.append(val)

    # def pop(self) -> None:
    #     main = self.stack.pop()
    #     if main == self.minimum[-1]:
    #         self.minimum.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()