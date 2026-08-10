'''
2026/08/10 daily challenge

depth first search + dynamic programming approach
'''


import math


class Solution:
    def __init__(self):
        self.dp = [None] * 100_001
        self.dp[0] = False

    def winnerSquareGame(self, n: int) -> bool:
        def dfs(i):
            if self.dp[i] is not None:
                return self.dp[i]
            for j in range(1, math.floor(i ** 0.5) + 1):
                if not dfs(i - j ** 2):
                    self.dp[i] = True
                    return True
            self.dp[i] = False
            return False

        return dfs(n)

