'''
2025/02/03 daily challenge

one-pass approach

maximize the length of subarray with running counter.
'''


import itertools


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = curr_inc = curr_dec = 1
        for a, b in itertools.pairwise(nums):
            if a > b:
                # decreasing
                max_len = max(max_len, curr_inc)
                curr_inc = 1
                curr_dec += 1
            elif a < b:
                # increasing
                max_len = max(max_len, curr_dec)
                curr_dec = 1
                curr_inc += 1
            else:
                max_len = max(max_len, curr_inc, curr_dec)
                curr_inc = curr_dec = 1
        return max(max_len, curr_inc, curr_dec)

