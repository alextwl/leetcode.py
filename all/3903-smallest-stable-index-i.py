'''
2026/09/04 daily challenge

prefix sums approach
'''


import itertools


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pmax = list(itertools.accumulate(nums, func=max))
        pmin = reversed(list(itertools.accumulate(reversed(nums), func=min)))

        for i, (p0, p1) in enumerate(zip(pmax, pmin)):
            if p0 - p1 <= k:
                return i

        return -1

