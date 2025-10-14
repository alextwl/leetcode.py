'''
2025/10/14 daily challenge

sliding window + set approach
'''


import collections


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        left = 0
        prev_end = set()  # the ending indices of previous subarrays

        for right, (a, b) in enumerate(itertools.pairwise(nums), start=1):
            if a >= b:
                left = right
            elif right - left + 1 == k:
                if (left - 1) in prev_end:
                    return True
                prev_end.add(right)
                left += 1
        return False

