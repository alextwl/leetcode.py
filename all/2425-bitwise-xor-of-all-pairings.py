'''
2024/01/16 daily challenge

XOR cancellation approach

check how can we cancel the duplicate parts in the bitwise XOR of all integers in nums3.
'''


import functools


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1) & 1:
            ans = functools.reduce(int.__xor__, nums2)
        if len(nums2) & 1:
            ans ^= functools.reduce(int.__xor__, nums1)
        return ans

