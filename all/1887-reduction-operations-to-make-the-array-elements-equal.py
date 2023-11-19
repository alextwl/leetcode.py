'''
2023/11/19 daily challenge

counter approach
'''

import collections


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        it = iter(sorted(counter.items(), reverse=True))
        
        # (largest, amount), but the largest is unused in further computation
        _, amount = next(it)

        ans = 0  # the number of operations
        modified_vars = 0  # the count of previously modified elements

        # (nextLargest, nextAmount)
        for _, nextAmount in it:
            modified_vars += amount
            ans += modified_vars
            amount = nextAmount

        return ans

