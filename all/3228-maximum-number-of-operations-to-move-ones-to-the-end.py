'''
2025/11/13 daily challenge

greedy method approach

the strategy to maximize the number of operations is
to always move the leftmost if possible.
'''


import itertools


class Solution:
    def maxOperations(self, s: str) -> int:
        gaps = 0 if s[-1] == '1' else 1
        ans = 0
        # iterate the string and count the gap reversely
        for prev, curr in itertools.pairwise(reversed(s)):
            if curr == '1':
                # we can do the same number of operations
                # as the number of gaps in the right side.
                ans += gaps
            elif prev != '0':
                # count a gap if curr == '0' and prev == '1'
                # if both curr & prev were '0', continue the gap.
                gaps += 1
        return ans

