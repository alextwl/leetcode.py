'''
similar to problem 1758.

change char only when the prev unchanged and
the difference of ASCII codes between prev & curr is < 2.
(which is so-called 'almost-equal'.)
'''


import itertools


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # case1: start from the first char unchanged
        prev0_changed = False
        ops0 = 0
        # case1: start from the first char which is changed
        prev1_changed = True
        ops1 = 1

        it = map(ord, word)
        prev = next(it)

        for v in it:
            diff = abs(v - prev)

            if prev0_changed:
                prev0_changed = False
            elif diff < 2:
                ops0 += 1
                prev0_changed = True

            if prev1_changed:
                prev1_changed = False
            elif diff < 2:
                ops1 += 1
                prev1_changed = True

            prev = v

        return min(ops0, ops1)

