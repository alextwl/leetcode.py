'''
2025/02/01 daily challenge

bitwise AND approach
'''


import itertools


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        for a, b in itertools.pairwise(nums):
            if (a & 1) == (b & 1):
                return False
        return True

