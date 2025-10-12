'''
2025/10/12 daily challenge

combinatorial + depth first search + dynamic programming approach

learnt from @karanagnani's solution:
https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/solutions/7267995/beats-99-explained/
'''


import functools
import math


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)

        @functools.cache
        def dfs(len_needed, odd_needed, i, carry):
            if len_needed < 0 or odd_needed < 0 or \
                    (len_needed + carry.bit_count()) < odd_needed:
                # invalid subsequence
                return 0
            if len_needed == 0:
                return int(odd_needed == carry.bit_count())
            if i >= n:
                # out of bound
                return 0
            
            ret = 0
            for takes in range(len_needed + 1):
                ways = math.comb(len_needed, takes) * \
                        pow(nums[i], takes, 1_000_000_007) % \
                        1_000_000_007
                new_carry = carry + takes
                ret = (ret + ways * \
                            dfs(len_needed - takes,
                                odd_needed - (new_carry & 1),
                                i + 1,
                                new_carry >> 1)) % 1_000_000_007
            return ret
        return dfs(m, k, 0, 0)

