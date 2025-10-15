'''
2025/10/15 daily challenge

two pointers approach

note a subarray can be also splitted into two subarrays.
'''


import itertools


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev_sublen = None  # previous length of a strictly increasing subarray
        max_k = 0
        left = 0
        for right, (a, b) in enumerate(itertools.pairwise(nums), start=1):
            if a >= b:
                last_sublen = right - left
                if prev_sublen is not None:
                    max_k = max(max_k,
                                min(prev_sublen, last_sublen),
                                max(prev_sublen, last_sublen) // 2)
                prev_sublen = last_sublen
                left = right
        # proceed the final subarray
        last_sublen = len(nums) - left
        if prev_sublen is not None:
            max_k = max(max_k,
                        min(prev_sublen, last_sublen),
                        max(prev_sublen, last_sublen) // 2)
        else:
            max_k = max(max_k, last_sublen // 2)
        return max_k

