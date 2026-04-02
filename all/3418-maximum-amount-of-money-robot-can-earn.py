'''
2026/04/02 daily challenge

dynamic programming approach
'''


import collections


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        # dp[i][j][pass_count] = maximum coins of (i-1, j-1) with remaining pass count
        dp = [[[float('-inf')] * 3 for _ in range(n+1)] for _ in range(m+1)]

        # init up & left cell of (0, 0) with zero.
        dp[0][1][2] = 0
        dp[1][0][2] = 0

        # process without neutralizing any robbers
        for i, row in enumerate(coins, start=1):
            for j, cell in enumerate(row, start=1):
                # max(up, left)
                dp[i][j][2] = max(dp[i-1][j][2], dp[i][j-1][2]) + cell

        # process with neutralized cases
        for cnt in [1, 0]:
            for i, row in enumerate(coins, start=1):
                for j, cell in enumerate(row, start=1):
                    # max(max(up, left) + cell, max(up & left with neutralize))
                    dp[i][j][cnt] = max(max(dp[i-1][j][cnt], dp[i][j-1][cnt]) + cell,
                                        max(dp[i-1][j][cnt+1], dp[i][j-1][cnt+1]))

        return max(dp[m][n])

