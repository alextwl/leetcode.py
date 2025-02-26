'''
2025/02/26 daily challenge

prefix sum approach

subtract minimum prefix (possibly zero or negative) from maximum prefix
and we get maximum absolute subarray sum.
'''


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = max_p = min_p = 0

        for v in nums:
            prefix_sum += v
            max_p = max(max_p, prefix_sum)
            min_p = min(min_p, prefix_sum)

        return max_p - min_p

