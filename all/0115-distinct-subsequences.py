'''
2026/09/06 daily challenge

dynamic programming approach
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            dp0, dp1 = dp[i], dp[i + 1]
            for j in range(m - 1, -1, -1):
                dp0[j] = dp1[j]  # dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp0[j] += dp1[j + 1]

        return dp[0][0]

