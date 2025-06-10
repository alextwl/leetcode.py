'''
2025/06/10 daily challenge

counter approach
'''


import collections


class Solution:
    def maxDifference(self, s: str) -> int:
        ctr = collections.Counter(s)
        max_odd, min_even = 0, float('inf')
        for v in ctr.values():
            if v & 1:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        return max_odd - min_even

