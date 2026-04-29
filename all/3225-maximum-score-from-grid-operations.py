'''
2026/04/29 daily challenge

dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/maximum-score-from-grid-operations/editorial/#approach-dynamic-programming

Runtime=4847ms, Beats=10.60%
time=O(n**3), space=O(n**3)
'''


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            # n*n==1, only one cell, unable to get any score.
            return 0
        
        # dp[c][h1][h2] = max score ending at column c with
        # h1 height of column (c - 1) and h2 height of column (c - 2).
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_sfx_max = [[0] * (n + 1) for _ in range(n + 1)]
        col_sum = [[0] * (n + 1) for _ in range(n)]

        # col_sum[c][r] = prefix sums from grid[0][c] to grid[r - 1][c]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]
        
        for i in range(1, n):
            for curr_height in range(n + 1):
                for prev_height in range(n + 1):
                    if curr_height <= prev_height:
                        extra_score = col_sum[i][prev_height] - col_sum[i][curr_height]
                        dp[i][curr_height][prev_height] = max(
                            dp[i][curr_height][prev_height],
                            prev_sfx_max[prev_height][0] + extra_score
                            )
                    else:
                        extra_score = col_sum[i - 1][curr_height] - col_sum[i - 1][prev_height]
                        dp[i][curr_height][prev_height] = max(
                            dp[i][curr_height][prev_height],
                            prev_sfx_max[prev_height][curr_height],
                            prev_max[prev_height][curr_height] + extra_score
                            )
            for curr_height in range(n + 1):
                prev_max[curr_height][0] = dp[i][curr_height][0]
                for prev_height in range(1, n + 1):
                    if prev_height > curr_height:
                        penalty = col_sum[i][prev_height] - col_sum[i][curr_height]
                    else:
                        penalty = 0
                    prev_max[curr_height][prev_height] = max(
                        prev_max[curr_height][prev_height - 1],
                        dp[i][curr_height][prev_height] - penalty
                        )
                prev_sfx_max[curr_height][n] = dp[i][curr_height][n]
                for prev_height in range(n - 1, -1, -1):
                    prev_sfx_max[curr_height][prev_height] = max(
                        prev_sfx_max[curr_height][prev_height + 1],
                        dp[i][curr_height][prev_height]
                        )
        ans = 0
        for k in range(n + 1):
            ans = max(ans, dp[n - 1][n][k], dp[n - 1][0][k])
        return ans

