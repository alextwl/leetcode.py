'''
2023/05/30 daily challenge

Knuth's multiplicative hash approach

https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing
'''

# a prime number for the hash function. randomly chosen.
P = 2097593  # also a Leyland prime.
# the raw bits of hash output. (e.g. W=5, output=h(c) & 0b11111)
W = 20
# the output bits (e.g. W=5, M=3, output=(h(c) & 0b11111)>>(5-3), 2 bits will be truncated.)
# since the question asks for 10**4 calls, choose a bigger number to reduce collisions.
M = 14


class MyHashSet:

    def __init__(self):
        # the number of leftmost hash output bits to be truncated.
        self.w_m = W - M
        '''
        buckets[h(c)] = [c, ...]
        use bucket to save the set because the hash function may have collision.
        '''
        self.buckets = [[] for _ in range(1<<M)]

    def h(self, key: int) -> int:
        # capture only W..(W-M) bits because we have limited buckets.
        return ((P * key) & (1<<W) - 1) >> self.w_m

    def add(self, key: int) -> None:
        target = self.buckets[self.h(key)]
        if key not in target:
            target.append(key)

    def remove(self, key: int) -> None:
        target = self.buckets[self.h(key)]
        if key in target:
            target.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self.h(key)]

