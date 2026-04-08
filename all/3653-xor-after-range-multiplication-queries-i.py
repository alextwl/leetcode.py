'''
2026/04/08 daily challenge

brute force approach
'''


import functools


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % 1_000_000_007
                idx += k
        return functools.reduce(int.__xor__, nums)

