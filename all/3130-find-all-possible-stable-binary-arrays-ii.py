'''
2026/03/10 daily challenge

dynamic programming approach

same to problem 3129 with larger input.
'''


MOD = 1_000_000_007


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        dp0 = dp[0]
        for j in range(min(one, limit) + 1):
            dp0[j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                excluded = dp[i - limit - 1][j][1] if i > limit else 0
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1] - excluded) % MOD
                excluded = dp[i][j - limit - 1][0] if j > limit else 0
                dp[i][j][1] = (dp[i][j-1][1] + dp[i][j-1][0] - excluded) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD

