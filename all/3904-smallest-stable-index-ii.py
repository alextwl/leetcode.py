'''
2026/09/05 daily challenge

prefix sums approach

since the amount of input might be large, we build only suffix mins in advance,
and then check each stability with running max.

same to problem 3903 with large input.
'''


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        rev_pmin = []
        curr_min = nums[-1]
        for v in reversed(nums):
            curr_min = min(curr_min, v)
            rev_pmin.append(curr_min)

        curr_max = nums[0]
        for i, (v, pmin) in enumerate(zip(nums, reversed(rev_pmin))):
            curr_max = max(curr_max, v)
            if curr_max - pmin <= k:
                return i

        return -1

