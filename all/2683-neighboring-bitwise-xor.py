'''
2025/01/17 daily challenge

bitwise XOR approach

there exists a valid original array only if we could cancel everything in derived.
'''

import functools


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return functools.reduce(int.__xor__, derived) == 0


'''
shortcut: since the input was an array containing only 0's and 1's,
          we can just count number which is 1's and
          extrapolate the final XOR result by parity.
'''


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return derived.count(1) & 1 != 1

