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

