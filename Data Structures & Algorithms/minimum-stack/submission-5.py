class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_value:
            self.min_value.append(val)
        # first iteration
        else:
            current_minimum = self.min_value[-1]
            self.min_value.append(min(current_minimum, val))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.min_value:
            self.min_value.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0
        
    def getMin(self) -> int:
        return self.min_value[-1]
