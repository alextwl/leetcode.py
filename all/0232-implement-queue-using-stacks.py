'''
2022/12/16 daily challenge

note the question asks for the implementation of a FIFO
with using only 2 stacks and limited operations.
'''

import collections

class MyQueue:

    def __init__(self):
        self.s1 = list()  # [newest cell, ..., oldest cell]
        self.s2 = list()  # [oldest cell, ..., newest cell]

    def push(self, x: int) -> None:
        '''
        use only append() & pop() functions to implement self.s1.insert(0, x)
        '''
        while(self.s1):
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while(self.s2):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1

