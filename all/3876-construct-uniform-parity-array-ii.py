'''
2026/09/03 daily challenge

math approach
'''


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        if min_val & 1:
            # if the minimum was an odd,
            # then we can eliminate all evens bigger than it.
            return True
        # the minimum is an even,
        # that means we cannot eliminate at least an odd once it appeared.
        # (consider we have no smaller odd subtracted from the smallest odd.)
        for v in nums1:
            if v & 1:
                return False
        return True

