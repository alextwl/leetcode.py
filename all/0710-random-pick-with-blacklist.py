'''
hashmap approach

remap blacklisted numbers which are smaller than n - len(blacklist).
'''


import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.blist = set(blacklist)
        self.mapping = dict()
        self.m = n - len(blacklist)
        new_num = self.m
        for v in blacklist:
            # remap blacklisted numbers < m
            if v < self.m:
                while new_num in blacklist:
                    new_num += 1
                self.mapping[v] = new_num
                new_num += 1

    def pick(self) -> int:
        r = random.randint(0, self.m - 1)
        return self.mapping[r] if r in self.blist else r

