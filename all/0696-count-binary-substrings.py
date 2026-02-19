'''
2026/02/19 daily challenge

sum the smaller lengthes of each pair of two consecutive groups.
'''


import itertools


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        it = itertools.groupby(s)
        prev = len(list(next(it)[1]))
        for _, group_iter in it:
            curr = len(list(group_iter))
            ans += min(prev, curr)
            prev = curr
        return ans

