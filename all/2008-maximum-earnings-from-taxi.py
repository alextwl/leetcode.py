'''
dynamic programming approach (bottom-up ver)

sort rides by start point, and maximize profits from end points.
'''


import collections


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # dp[i] = maximum profits at point i
        dp = [0] * (n + 1)
        # start2rides[start] = [(end, profit), ...]
        start2rides = collections.defaultdict(list)
        for start, end, tip in rides:
            start2rides[start].append((end, end - start + tip))

        for i in range(n - 1, 0, -1):
            curr_max_profit = dp[i]
            for end, profit in start2rides[i]:
                curr_max_profit = max(curr_max_profit, dp[end] + profit)
            # max(with a ride, no ride from i+1)
            dp[i] = max(curr_max_profit, dp[i + 1])

        return dp[1]

