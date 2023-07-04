'''
2023/07/04 daily challenge

bitwise approach

learnt from a super-detailed explanation:
https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

for the problem Single Number II, its parameter is k=3, p=1.
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        k = 3,
        so m = math.ceil(math.log2(3)) = 2 counters.

        since 2^m > k, we also need a mask.
        '''
        x1 = x2 = 0
        mask = 0

        for v in nums:
            x2 ^= x1 & v
            x1 ^= v

            mask = ~(x1 & x2)  # because k = 3 = 0b11

            x2 &= mask
            x1 &= mask

        return x1  # because p = 0b01, so we return x1, or (x1 | x2) regardless of p.

