'''
2026/10/23 daily challenge

bitwise AND + math approach

learnt from official editorial:
https://leetcode.com/problems/maximum-k-to-sort-a-permutation/editorial/#approach-traverse-and-compute-the-bitwise-and

all unsorted elements must have k's setbits.
'''


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1  # == all 1's bits
        for i, v in enumerate(nums):
            if v == i:
                # nums[i] is sorted.
                continue
            k = k & v
        if k == -1:
            # nums is already sorted.
            return 0
        return k

