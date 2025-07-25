'''
2025/07/25 daily challenge

counter approach

it's equivalent to "max unique subsequence sum",
pick all unique non-negative elements or just the maximum negative element.
'''


import collections


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        max_sum = 0
        for v in cnt.keys():
            if v > 0:
                max_sum += v
        return max_sum if max_sum > 0 else max(cnt.keys())

