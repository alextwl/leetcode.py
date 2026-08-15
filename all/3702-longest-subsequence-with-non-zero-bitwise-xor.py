'''
2026/08/15 daily challenge

bitwise XOR approach
'''


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        nonzero = 0
        xor = 0
        for v in nums:
            if v:
                nonzero += 1
                xor ^= v
        
        if nonzero == 0:
            # cannot make a non-zero subsequence
            return 0

        # if the bitwise XOR of entire array was zero,
        # remove a nonzero value.
        return len(nums) - (xor == 0)

