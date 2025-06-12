'''
2025/06/12 daily challenge
'''


import itertools


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        return max(abs(a - b) for a, b in itertools.pairwise(nums))

