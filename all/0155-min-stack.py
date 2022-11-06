class MinStack:
    def __init__(self):
        # each element is a tuple of (pushed val, current minimum val of stack)
        # in order to achieve time=O(1)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # first element has minimum val
            self.stack.append((val, val))
        else:
            # push & compare val with last minimum val
            self.stack.append((val, min(self.stack[-1][1],val)))

    def pop(self) -> None:
        # didn't check stack empty,
        # all funcs except push will always be called on non-empty stacks.
        self.stack.pop()

    def top(self) -> int:
        # return last val of stack
        return self.stack[-1][0]

    def getMin(self) -> int:
        # return minimal val of stack
        return self.stack[-1][1]
