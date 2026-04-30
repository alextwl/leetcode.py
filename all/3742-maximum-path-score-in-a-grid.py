'''
2026/04/30 daily challenge

dynamic programming approach (knapsack-like problem)

learnt from official editorial:
https://leetcode.com/problems/maximum-path-score-in-a-grid/editorial/#approach-dynamic-programming
'''


import collections


NEG_INF = float('-inf')


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j][cost]
        dp = [[[NEG_INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0  # constraint: grid[0][0] == 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == NEG_INF:
                        continue

                    if i + 1 < m:
                        # move down
                        val = grid[i + 1][j]
                        cost = 1 if val else 0
                        next_c = c + cost
                        if next_c <= k:
                            dp[i + 1][j][next_c] = max(dp[i + 1][j][next_c], dp[i][j][c] + val)

                    if j + 1 < n:
                        # move right
                        val = grid[i][j + 1]
                        cost = 1 if val else 0
                        next_c = c + cost
                        if next_c <= k:
                            dp[i][j + 1][next_c] = max(dp[i][j + 1][next_c], dp[i][j][c] + val)
        ans = max(dp[-1][-1])
        return -1 if ans < 0 else ans

