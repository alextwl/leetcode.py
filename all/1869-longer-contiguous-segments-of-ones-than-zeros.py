'''
group consecutive chars and find the maximums.
'''


import itertools


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_len = {'0': 0, '1': 0}
        for c, it in itertools.groupby(s):
            max_len[c] = max(max_len[c], len(list(it)))
        return max_len['1'] > max_len['0']

