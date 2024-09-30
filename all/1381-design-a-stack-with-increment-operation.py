'''
2024/09/30 daily challenge

tracking increment history
'''


class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []  # (val, serial_number)
        self.next_sn = 1
        self.increments = []  # (val, left, right)

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append((x, self.next_sn))
            self.next_sn += 1

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        val, sn = self.stack.pop()

        for inc, left, right in self.increments:
            if left <= sn <= right:
                val += inc

        return val

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.increments.append((val, self.stack[0][1], self.stack[min(k, len(self.stack)) - 1][1]))

