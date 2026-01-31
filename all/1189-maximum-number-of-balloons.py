'''
counter approach

same to problem 2287.
'''


import collections


BALLOON = collections.Counter("balloon")


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ctr = collections.Counter(text)
        return min(ctr[c] // div for c, div in BALLOON.items())

