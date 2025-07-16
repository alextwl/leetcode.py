'''
2025/07/16 daily challenge

dynamic programming approach
'''


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # max length of subsequence of mod 0/1 with even/odd ending
        mod0_even = mod0_odd = 0
        mod1_even = mod1_odd = 0

        for v in nums:
            if v & 1:
                # it's odd
                # odd + odd = mod0 ending with odd
                mod0_odd += 1
                # even + odd = mod1 ending with odd
                mod1_odd = mod1_even + 1
            else:
                # it's even
                # even + even = mod0 ending with even
                mod0_even += 1
                # odd + even = mod1 ending with even
                mod1_even = mod1_odd + 1

        return max(mod0_even, mod0_odd, mod1_even, mod1_odd)

