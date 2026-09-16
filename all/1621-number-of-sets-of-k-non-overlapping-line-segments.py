'''
2026/09/16 daily challenge

prefix sums + dynamic programming approach
'''


MOD = 1_000_000_007


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [1] * n  # dp[i] = number of ways ending at point i.
        pfx = [0] * (n + 1)

        for i, dp_i in enumerate(dp):
            pfx[i + 1] = (pfx[i] + dp_i) % MOD

        # pick each segment and accumulate ways of combinations
        for _ in range(k):
            dp[0] = 0  # no valid segment for only 1 point.
            for i in range(1, n):
                dp[i] = (dp[i - 1] + pfx[i]) % MOD
            for i in range(n):
                pfx[i + 1] = (pfx[i] + dp[i]) % MOD

        return dp[-1]

