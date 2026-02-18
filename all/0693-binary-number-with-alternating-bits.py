'''
2026/02/18 daily challenge
'''


import itertools


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(a != b for a, b in itertools.pairwise(bin(n)[2:]))

