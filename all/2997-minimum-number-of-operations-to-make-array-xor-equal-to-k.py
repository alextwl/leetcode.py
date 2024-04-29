'''
2024/04/29 daily challenge

XOR approach

XOR everything and count the different bits.
'''


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for v in nums:
            k ^= v
        return k.bit_count()


'''
oneliner ver
'''


import functools


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return functools.reduce(int.__xor__, nums, k).bit_count()

