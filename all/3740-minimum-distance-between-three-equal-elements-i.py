'''
2026/04/10 daily challenge

sliding window approach
'''

import collections


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_window = 101
        # seen_idx[val] = [idx, idx, ...]
        seen_idx = collections.defaultdict(list)
        for i, v in enumerate(nums):
            if len(seen_idx[v]) >= 2:
                min_window = min(min_window, i - seen_idx[v][-2])
            seen_idx[v].append(i)
        # abs(i-j) + abs(j-k) + abs(k-i) == (max(i,j,k) - min(i,j,k)) * 2
        return -1 if min_window == 101 else min_window * 2

