'''
set approach
'''


import functools


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(functools.reduce(lambda x, y: set(x) & set(y), nums))

