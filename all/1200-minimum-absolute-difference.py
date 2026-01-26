'''
2026/01/26 daily challenge
'''


import itertools


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 2_000_002
        ans = []
        for a, b in itertools.pairwise(arr):
            diff = b - a
            if diff < min_diff:
                min_diff = diff
                ans = [[a, b]]
            elif diff == min_diff:
                ans.append([a, b])
        return ans

