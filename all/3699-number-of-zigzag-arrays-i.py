'''
2026/06/23 daily challenge

dynamic programming + prefix sums approach

learnt from official editorial:
https://leetcode.com/problems/number-of-zigzag-arrays-i/editorial/#approach-dynamic-programming--prefix-sum-optimization

time=O(mn), space=O(m)
8632ms, Beats 26.32%
'''


import itertools


MOD = 1_000_000_007


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        dp0 = [1] * m
        dp1 = [1] * m
        for _ in range(n - 1):
            # prefix sums
            sum0 = list(itertools.accumulate(dp0, initial=0))
            sum1 = list(itertools.accumulate(dp1, initial=0))

            dp0 = [x % MOD for x in sum1[:-1]]
            sum0_m = sum0[-1]
            dp1 = [(sum0_m - x) % MOD for x in sum0[1:]]
        return (sum(dp0) + sum(dp1)) % MOD


'''
optimized dynamic programming + prefix sums approach

half the computations by counting only present parity of array length conditionally.

3210ms
'''


import itertools


MOD = 1_000_000_007


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        dp = [1] * (m + 1)  # 1-indexed
        dp[0] = 0  # dummy case

        for i in range(2, n + 1):
            if i & 1:
                # odd length array
                pfx = list(itertools.accumulate(dp))
                pfx_m = pfx[-1]
                # dp[v] = sum(pfx_m - x for u, x in enumerate(dp) if u > v) = pfx_m - pfx[v]
                dp = [0] + [(pfx_m - x) % MOD for x in pfx[1:]]
            else:
                # even length array, for u < v
                # dp[v] = sum(x for u, x in enumerate(dp) if u < v) = prefix_sum[v]
                # note this prefix sum init with 0, pfx[0] = 0
                dp = list(itertools.accumulate(dp, initial=0))[:-1]

        # double valid seqs for symmetry
        return (sum(dp) % MOD * 2) % MOD


'''
dynamic programming approach (time limit exceeded)

time=O(nr), space=O(r)
'''


MOD = 1_000_000_007


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        dp0 = [[i, i] for i in range(r + 1)]
        dp1 = [[0, 0] for i in range(r + 1)]

        for i in range(n - 1, 0, -1):
            dp1[l - 1][0] = 0
            dp1[l - 1][1] = 0
            for j in range(l, r + 1):
                dp1[j][0] = (dp1[j - 1][0] + dp0[j - 1][1] - dp0[l - 1][1]) % MOD
                dp1[j][1] = (dp1[j - 1][1] + dp0[r][0] - dp0[j][0]) % MOD
            dp0, dp1 = dp1, dp0

        return (dp0[r][0] + dp0[r][1]) % MOD

