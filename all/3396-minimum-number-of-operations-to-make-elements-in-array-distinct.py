'''
2025/04/08 daily challenge

set approach

scan the array reversely and find the first occurance of duplicate.
'''


import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i, v in enumerate(reversed(nums)):
            if v in seen:
                return math.ceil((len(nums) - i) / 3)
            seen.add(v)
        return 0

