'''
2024/01/27 daily challenge

dynamic programming approach (recursive)
'''

import functools


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @functools.cache
        def dp(n, k):
            if k < 0 or n < 0:
                # no way to consist of numbers with out-of-bound parameters
                return 0
            if n == 0:
                # there's exactly one way to consist of single number with zero inverse pairs,
                # or there's no way with k>0 inverse pairs.
                return 1 if k == 0 else 0
            
            if k == 0:
                # no more pairs to be picked, so there's one valid way.
                return 1
            
            # A: n-th number picked for pairs
            # B: n-th number skipped
            # C: the gap between A and B
            # ans = A + B - C
            return (dp(n, k-1) + dp(n-1, k) - dp(n-1, k-n)) % 1_000_000_007
        
        return dp(n, k)


'''
dynamic programming approach (iterative)
'''


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp1 = [0] * (k+1)
        dp1[0] = 1
        
        for i in range(1, n+1):
            dp0, dp1 = dp1, [1]
            for remain in range(1, k+1):
                gap = 0 if remain < i else dp0[remain - i]
                # pick + skip - gap
                dp1.append((dp1[-1] + dp0[remain] - gap) % 1_000_000_007)

        return dp1[-1]

