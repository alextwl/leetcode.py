'''
2026/04/05 daily challenge

counter approach

robot returns to the origin when
the counts of opposite direction moves are equal.
'''


import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ctr = collections.Counter(moves)
        return ctr['R'] == ctr['L'] and ctr['U'] == ctr['D']

