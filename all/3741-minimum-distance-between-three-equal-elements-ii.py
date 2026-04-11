'''
2026/04/11 daily challenge

memorization (fixed-size index queues for all possible values) approach

preallocation improves performance significantly.

same to problem 3740.
'''


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        v0_idx = [-1] * (len(nums) + 1)
        v1_idx = [-1] * (len(nums) + 1)

        min_window = 100_001
        for i, v2 in enumerate(nums):
            if v0_idx[v2] > -1:
                min_window = min(min_window, i - v0_idx[v2])
            v0_idx[v2], v1_idx[v2] = v1_idx[v2], i

        return -1 if min_window == 100_001 else min_window * 2

