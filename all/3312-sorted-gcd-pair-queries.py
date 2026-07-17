'''
2026/07/17 daily challenge

inclusion-exclusion principle + prefix sums + binary search approach

learnt from official editorial:
https://leetcode.com/problems/sorted-gcd-pair-queries/editorial/#approach-inclusion-exclusion-principle--prefix-sum--binary-search
'''


import bisect


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # build prefix counter of divisors
        ctr = [0] * (max_val + 1)
        for v in nums:
            ctr[v] += 1

        # inclusion
        for x in range(1, max_val + 1):
            for y in range(x * 2, max_val + 1, x):
                ctr[x] += ctr[y]
        
        for x in range(1, max_val + 1):
            ctr[x] = ctr[x] * (ctr[x] - 1) // 2

        # exclusion
        for x in range(max_val, 0, -1):
            for y in range(x * 2, max_val + 1, x):
                ctr[x] -= ctr[y]
        
        for x in range(1, max_val + 1):
            ctr[x] += ctr[x - 1]

        gcd_pairs = [bisect.bisect_left(ctr, q + 1) for q in queries]

        return gcd_pairs

