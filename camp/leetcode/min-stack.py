class MinStack:

    def __init__(self):
        self.stack = []
        self._min = float('inf')
        
    def push(self, val: int) -> None:
        self._min = min(self._min, val)
        self.stack.append([val, self._min])  
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self._min = self.stack[-1][1]
        else:
            self._min = float('inf')
        
        
    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()