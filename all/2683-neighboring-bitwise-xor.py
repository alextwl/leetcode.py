'''
2025/01/17 daily challenge

bitwise XOR approach

there exists a valid original array only if we could cancel everything in derived.
'''

import functools


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return functools.reduce(int.__xor__, derived) == 0

