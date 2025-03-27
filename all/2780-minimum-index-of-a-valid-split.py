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


'''
Boyer-Moore majority voting algorithm approach

learnt from official editorial 2:
https://leetcode.com/problems/minimum-index-of-a-valid-split/editorial/#approach-2-boyer-moore-majority-voting-algorithm
'''


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # find the dominant element by majority voting algorithm
        n = len(nums)
        x = nums[0]
        major_count = 0

        for v in nums:
            if v == x:
                major_count += 1
            else:
                major_count -= 1
            if major_count == 0:
                x = v
                major_count = 1

        # the majority might change during the search and
        # we cannot count the total number of final majority element simutaneously,
        # so we run the 2nd pass to count it.
        total_dom = sum(v == x for v in nums)

        # try to split
        dom_count = 0
        for i, v in enumerate(nums):
            if v == x:
                dom_count += 1
                if dom_count > ((i + 1) >> 1) and (total_dom - dom_count) > ((n - i - 1) >> 1):
                    return i
        return -1

