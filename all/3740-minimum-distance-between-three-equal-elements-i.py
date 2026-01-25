'''
sliding window approach
'''


import collections


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_window = 101
        g = collections.defaultdict(list)
        for i, v in enumerate(nums):
            g[v].append(i)
        for indices in g.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                min_window = min(min_window, indices[i + 2] - indices[i])
        return -1 if min_window == 101 else min_window * 2

