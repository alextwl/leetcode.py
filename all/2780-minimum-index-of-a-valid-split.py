'''
2025/03/27 daily challenge

counter approach
'''


import collections


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # exactly one dominant in nums is guaranteed,
        # it means the dominant is more than half the elements.
        # no matter where we split the array,
        # at least one subarray has the same dominant.
        dom, total_dom = collections.Counter(nums).most_common(1)[0]

        dom_count = 0
        for i, v in enumerate(nums):
            if v == dom:
                dom_count += 1
                # check if both sides had more than half the dominants of subarrays.
                if dom_count > ((i + 1) >> 1) and (total_dom - dom_count) > ((n - i - 1) >> 1):
                    return i
        return -1

