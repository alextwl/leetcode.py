'''
2025/10/28 daily challenge

prefix sum approach
'''


import itertools


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix = itertools.accumulate(nums)
        suffix = list(itertools.accumulate(reversed(nums)))
        ans = 0
        for v, p, s in zip(nums, prefix, reversed(suffix)):
            if v == 0:
                if p == s:
                    # if the prefix sum was equivalent to the suffix one,
                    # both directions at curr are valid.
                    ans += 2
                elif abs(p - s) == 1:
                    # if the difference between the prefix and suffix was 1,
                    # one direction at curr is valid.
                    ans += 1
        return ans

