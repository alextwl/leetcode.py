'''
2025/02/06 daily challenge

product frequency counter + math approach
'''


import collections
import functools


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = collections.defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prods[nums[i] * nums[j]] += 1

        @functools.cache
        def compute_ways(freq):
            '''
            the number of ways to choose 2 pairs * each pair can form 8 tuples:

            (freq - 1) * freq
            ----------------- * 8
                    2
            '''
            return (freq - 1) * freq // 2 * 8

        ans = 0
        for v in prods.values():
            # only two or more pairs can form tuples
            if v > 1:
                ans += compute_ways(v)

        return ans

