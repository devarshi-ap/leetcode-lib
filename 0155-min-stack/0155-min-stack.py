class MinStack:

    def __init__(self):
        # [(value, min_so_far), ...]
        self.stack = []

    def push(self, value: int) -> None:
        # push tuple onto stack
        if not self.stack:
            # empty stack, set min
            self.stack.append((value, value))
        else:
            # not empty stack, compare value to current_min to set min_so_far
            current_min = self.stack[-1][1]
            self.stack.append((value, min(value, current_min)))

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