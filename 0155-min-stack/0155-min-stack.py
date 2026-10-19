class MinStack:

    def __init__(self):
        # [(value, min_so_far), ...]
        self.stack = []

    def push(self, value: int) -> None:
        # update current_min, then push tuple onto stack
        current_min = value if not self.stack else min(value, self.stack[-1][1])
        self.stack.append((value, current_min))

    def pop(self) -> None:
        # remove topmost value from stack (pop from back)
        self.stack.pop()

    def top(self) -> int:
        # return topmost value (~ peek)
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        # return latest min_so_far
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()