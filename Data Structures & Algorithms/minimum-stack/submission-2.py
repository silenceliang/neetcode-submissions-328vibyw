class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        if self.stack:
            _, min_val = self.stack[-1]
            self.stack.append([val, min(min_val, val)])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        _, min_val = self.stack[-1]
        return min_val
