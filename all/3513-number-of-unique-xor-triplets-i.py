'''
2026/07/23 daily challenge

XOR pattern matching approach
'''


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # note the nums array is a permutation of [1, n],
        # makes every number in that range appears exactly once.
        n = len(nums)
        if n < 3:
            # n=1, xor=[1]
            # n=2, xor=[1, 2]
            return n

        # for n >= 3, given 2**k <= n < 2**(k+1),
        # assume all [0, 2**(k+1) - 1] numbers can be formed by an XOR triplet.
        # 1 ^ 2 ^ 3 == 0
        # 1 ^ 1 ^ 1 == 1
        # 1 ^ 1 ^ n == n
        # and for all x in [n+1, 2**k - 1],
        # when we subtract (xor) 2**k from x, we have x ^ 2**k = y
        # (equivalent to remove the rightmost bit from x),
        # y is smaller than 2**k, we can have (a, b, 2**k) triplet to form x:
        # if y != 1:
        #   a, b = 1, 1 ^ y
        # elif y == 1:
        #   a, b = 2, 3  # because 2 ^ 3 == 1
        # so we can construct all numbers in [0, 2**(k+1) - 1], the answer is 2**(k+1).
        return 1 << n.bit_length()

