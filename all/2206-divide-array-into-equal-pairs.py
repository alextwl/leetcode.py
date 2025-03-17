'''
2025/03/17 daily challenge

counter approach
'''


import collections


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return not any(v & 1 for v in collections.Counter(nums).values())

