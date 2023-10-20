'''
2023/10/20 daily challenge

stack approach

both next() & hasNext() check the existence of next element.
'''


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, -1]]
        self.next_prepared = False
    
    def next(self) -> int:
        if not self.next_prepared:
            if not _prepare_next():
                raise StopIteration()

        self.next_prepared = False
        elm, pos = self.stack[-1]
        return elm[pos].getInteger()

    def hasNext(self) -> bool:
        if self.next_prepared:
            return True

        return self._prepare_next()

    def _prepare_next(self) -> bool:
        while(self.stack):
            elm, pos = self.stack[-1]
            pos += 1
            if pos >= len(elm):
                self.stack.pop()
                continue
            self.stack[-1][1] = pos

            if elm[pos].isInteger():
                self.next_prepared = True
                return True

            self.stack.append([elm[pos].getList(), -1])

        return False

