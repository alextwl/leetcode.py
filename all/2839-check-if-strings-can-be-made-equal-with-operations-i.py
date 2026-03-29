'''
2026/03/29 daily challenge

set approach
'''


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return set(s1[::2]) == set(s2[::2]) and set(s1[1::2]) == set(s2[1::2])

