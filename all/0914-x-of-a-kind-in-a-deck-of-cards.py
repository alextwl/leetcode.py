'''
counter + greatest common divisor (GCD) approach

only GCD > 1 of all frequencies of each distinct card can be partitioned.
'''


import collections
import math


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*set(collections.Counter(deck).values())) > 1

