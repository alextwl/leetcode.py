'''
2024/01/04 daily challenge

counter approach (math problem)

if there's a unique element in the array,
it's not possible to make array empty.
'''

import collections
import functools


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        
        if 1 in counts.values():
            return -1
        
        @functools.cache
        def min_ops(v):
            quo, rem = divmod(v, 3)
            if quo:
                if rem:
                    # for 3*q + 2*1 and for 3*(q-1) + 2*2
                    return quo + 1
                # for 3*q
                return quo

            # for 2*1
            return 1

        ans = 0        
        for v in counts.values():
            ans += min_ops(v)

        return ans

