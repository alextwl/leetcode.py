'''
2025/02/04 daily challenge

one-pass approach
'''


import itertools


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for a, b in itertools.pairwise(nums):
            if a >= b:
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0
            curr_sum += b
        return max(max_sum, curr_sum)

