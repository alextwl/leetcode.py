'''
2026/10/31 daily challenge

dynamic programming approach
'''


MOD = 1_000_000_007


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[x][y][0=from left, 1=from up]
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                # let mirror inherit path count from only one source respectively.
                if i:
                    dp[i][j][0] = ((dp[i-1][j][0] if grid[i-1][j] == 0 else 0) + dp[i-1][j][1]) % MOD
                if j:
                    dp[i][j][1] = ((dp[i][j-1][1] if grid[i][j-1] == 0 else 0) + dp[i][j-1][0]) % MOD

        return (dp[-1][-1][0] + dp[-1][-1][1]) % MOD

