'''
2023/10/20 daily challenge

stack approach

always move the pointer to the next element in advance when hasNext() is invoked,
so that the rightmost element of stack is guaranteed an integer element.
'''


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, -1]]
    
    def next(self) -> int:
        elm, pos = self.stack[-1]
        return elm[pos].getInteger()

    def hasNext(self) -> bool:
        while(self.stack):
            elm, pos = self.stack[-1]
            pos += 1
            if pos >= len(elm):
                self.stack.pop()
                continue
            self.stack[-1][1] = pos

            if elm[pos].isInteger():
                return True

            self.stack.append([elm[pos].getList(), -1])

        return False

