'''
linear search approach

the pointer stops accumulating when encounters a null value.
'''


class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.stream = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if self.stream[self.ptr] is None:
            return []
        ret = []
        for i in range(self.ptr, self.n + 1):
            if self.stream[i] is None:
                break
            ret.append(self.stream[i])
        self.ptr = i
        return ret

