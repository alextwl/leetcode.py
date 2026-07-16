'''
2026/07/16 daily challenge

simulation approach
'''


import itertools
import math


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        pfx_gcd = []
        for v, vmax in zip(nums, itertools.accumulate(nums, func=max)):
            pfx_gcd.append(math.gcd(v, vmax))

        pfx_gcd.sort()
        ans = 0
        for v0, v1 in zip(pfx_gcd[:n//2], pfx_gcd[-1:n//2-1:-1]):
            ans += math.gcd(v0, v1)
        return ans

