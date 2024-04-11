'''
2024/04/11 daily challenge

monotonic stack approach
'''

import collections


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # use deque instead of stack here because we need to remove leading zeroes later
        q = collections.deque()

        # stage 1: try to remove digits in order to approach
        # the smallest number as sorted digits by non-decreasing order
        for digit in num:
            while k and q and digit < q[-1]:
                # the previous digit shouldn't be greater than current digit,
                # remove it.
                q.pop()
                k -= 1
            q.append(digit)

        # stage 2: truncate from the rightmost
        # if there're still k remaining digits to be removed
        for _ in range(k):
            q.pop()

        # remove leading zeroes
        while q and q[0] == '0':
            q.popleft()

        # concatenate q or return zero if it's empty
        return ''.join(q) if q else '0'

