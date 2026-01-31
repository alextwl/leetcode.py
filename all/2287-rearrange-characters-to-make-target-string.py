'''
counter approach

same to problem 1189.
'''


import collections


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ctr = collections.Counter(s)
        return min(ctr[c] // div for c, div in collections.Counter(target).items())

