'''
2025/07/27 daily challenge

group all consecutive equal elements and compare with neighbor groups.
'''


import itertools


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # deduplication
        x = [v for v, _ in itertools.groupby(nums)]
        ans = sum(v0 > v1 < v2 or v0 < v1 > v2 for v0, v1, v2 in zip(x, x[1:], x[2:]))
        return ans

