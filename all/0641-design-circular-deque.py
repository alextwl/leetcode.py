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


'''
linked-list approach
'''


class Node:
    def __init__(self, value, parent = None, child = None):
        self.value = value
        self.parent = parent
        self.child = child


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.root = Node(-1)
        self.term = Node(-1, parent=self.root)
        self.root.child = self.term

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        obj = Node(value, parent=self.root, child=self.root.child)
        self.root.child.parent = obj
        self.root.child = obj
        self.len += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        obj = Node(value, parent=self.term.parent, child=self.term)
        self.term.parent.child = obj
        self.term.parent = obj
        self.len += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.root.child = self.root.child.child
        self.root.child.parent = self.root
        self.len -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.term.parent.parent.child = self.term
        self.term.parent = self.term.parent.parent
        self.len -= 1
        
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.root.child.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.term.parent.value

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len >= self.k

