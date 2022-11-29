'''
2022/11/29 daily challenge

use python's builtin structure/functions with time complexity near O(1) avg.

since RandomizedSet is a **set**, which means each value in the set is unique,
we will be able to use dict to access the index of value to be removed in O(1) average.
'''

import random


class RandomizedSet:

    def __init__(self):
        self.values = list()
        self.dict2index = dict()

    def insert(self, val: int) -> bool:
        if val not in self.dict2index:
            self.values.append(val)
            self.dict2index[val] = len(self.values) - 1
            return True
        # val already exists.
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict2index:
            '''
            move the last value in self.values to the position of input val
            in order to keep the indexes unmodified in self.dict2index.
            '''
            self.values[self.dict2index[val]], self.dict2index[self.values[-1]] = self.values[-1], self.dict2index[val]
            del self.values[-1]
            del self.dict2index[val]
            return True
        # val not found
        return False

    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values)-1)]

