'''
2025/08/12 daily challenge

dynamic programming + tabulation approach
'''


POWERS = {1: [i for i in range(1, 301)],
          2: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
              121, 144, 169, 196, 225, 256, 289],
          3: [1, 8, 27, 64, 125, 216],
          4: [1, 16, 81, 256],
          5: [1, 32, 243]}


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n+1)
        # base case
        dp[0] = 1
        
        # each elements in the sum should be **unique** positive integers
        for p in POWERS[x]:
            for i in range(n, p-1, -1):
                dp[i] = (dp[i] + dp[i - p]) % 1_000_000_007
        
        return dp[-1]


'''
recursion approach
'''


import functools


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        bmax = n ** (1 / x) + 1   # max value of the base

        @functools.cache
        def dp(n, b):
            if b > bmax:
                return 0
            rem = n - b ** x
            if rem < 0:
                # out of range
                return 0
            if rem == 0:
                return 1
            return (dp(rem, b + 1) + dp(n, b + 1)) % 1_000_000_007
        return dp(n, 1)

