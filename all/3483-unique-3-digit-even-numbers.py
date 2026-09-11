'''
2026/09/11 daily challenge

counter (brute force) approach
'''


import collections


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        copies = collections.Counter(digits)
        return sum(collections.Counter(map(int, str(v))) <= copies for v in range(100, 999, 2))

