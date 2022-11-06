'''
2022/09/25 daily challenge
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.maxlen = k
        self._front = 0
        self._rear = 0
        self._len = 0
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self._len == self.maxlen:
            return False
        self._len += 1

        self.q[self._rear] = value
        self._rear += 1
        if self._rear == self.maxlen:
            self._rear = 0

        return True

    def deQueue(self) -> bool:
        if self._len == 0:
            return False
        self._len -= 1
        
        self._front += 1
        if self._front == self.maxlen:
            self._front = 0
        
        return True

    def Front(self) -> int:
        if self._len:
            return self.q[self._front]
        else:
            return -1

    def Rear(self) -> int:
        if self._len:
            return self.q[self._rear - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self._len == 0

    def isFull(self) -> bool:
        return self._len == self.maxlen

