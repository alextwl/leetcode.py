'''
2025/11/13 daily challenge

greedy method approach (count gaps reversely)

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


'''
count ones ver
'''


import itertools


class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 1 if s[0] == '1' else 0
        ans = 0

        for prev, curr in itertools.pairwise(s):
            if curr == '1':
                ones += 1
            elif prev != '0':
                # a new gap is opened, accumulate the number of operations
                ans += ones

        return ans

