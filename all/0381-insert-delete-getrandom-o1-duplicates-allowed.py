'''
similar to the problem 380.

See https://wiki.python.org/moin/TimeComplexity for python builtin's time complexity
'''

import collections
import random

class RandomizedCollection:

    def __init__(self):
        self.values = list()
        self.d2i = collections.defaultdict(set)  # self.d2i[value] returns a set of indexes

    def insert(self, val: int) -> bool:
        # duplicates allowed, but we also need to return if it's already existed or not.
        already_present = not(self.d2i[val])
        self.values.append(val)
        self.d2i[val].add(len(self.values)-1)
        return already_present

    def remove(self, val: int) -> bool:
        if self.d2i[val]:
            '''
            move last value to one of the val's position,
            unless the value to be popped is the last value.
            '''
            target_index = self.d2i[val].pop()
            if target_index < len(self.values) - 1:
                last_value = self.values[-1]
                self.values[target_index] = last_value
                self.d2i[last_value].remove(len(self.values)-1)
                self.d2i[last_value].add(target_index)
            self.values.pop()
            return True
        # val not found.
        return False

    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values)-1)]

