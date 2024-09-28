'''
2024/09/28 daily challenge

stack approach
'''


class MyCircularDeque:
    def __init__(self, k: int):
        self.q1 = []
        self.q2 = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        while self.q1:
            self.q2.append(self.q1.pop())
        self.q2.append(value)

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        while self.q2:
            self.q1.append(self.q2.pop())
        self.q1.append(value)
        
        return True

    def deleteFront(self) -> bool:
        while self.q1:
            self.q2.append(self.q1.pop())
        if self.q2:
            self.q2.pop()
            return True
        return False

    def deleteLast(self) -> bool:
        while self.q2:
            self.q1.append(self.q2.pop())
        if self.q1:
            self.q1.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.q1:
            return self.q1[0]
        elif self.q2:
            return self.q2[-1]
        return -1

    def getRear(self) -> int:
        if self.q2:
            return self.q2[0]
        elif self.q1:
            return self.q1[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0

    def isFull(self) -> bool:
        return len(self.q1) + len(self.q2) >= self.k

