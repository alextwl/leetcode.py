'''
2024/11/05 daily challenge

compare each pair of two consecutive elements and count if it's different.
'''


class Solution:
    def minChanges(self, s: str) -> int:
        return sum(a != b for a, b in zip(s[::2], s[1::2]))


'''
only for Python>=3.12
'''

import itertools


class Solution:
    def minChanges(self, s: str) -> int:
        return sum(a != b for a, b in itertools.batched(s, n=2))

