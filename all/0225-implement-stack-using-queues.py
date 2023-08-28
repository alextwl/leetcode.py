'''
2023/08/28 daily challenge

two queues approach
'''

import collections


class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q1:
            self.q1, self.q2 = self.q2, self.q1
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        return self.q1.popleft()
        
    def top(self) -> int:
        topval = self.pop()
        self.q2.append(topval)
        return topval

    def empty(self) -> bool:
        return False if self.q1 or self.q2 else True

