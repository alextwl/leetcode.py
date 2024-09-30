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


'''
lazy propagation approach

all operations are in O(1) time.

learnt from official solution 3:
https://leetcode.com/problems/design-a-stack-with-increment-operation/solution/
'''


class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize
        self.top = -1  # the index of top element in stack, -1 means empty.

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top < 0:
            return -1
        
        # pop the top element with increment
        ans = self.stack[self.top] + self.inc[self.top]
        
        # add the last increment to the 2nd increment after top element popped
        if self.top > 0:
            self.inc[self.top - 1] += self.inc[self.top]

        # reset the popped increment
        self.inc[self.top] = 0

        self.top -= 1
        return ans

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0:
            i = min(self.top, k - 1)
            self.inc[i] += val

