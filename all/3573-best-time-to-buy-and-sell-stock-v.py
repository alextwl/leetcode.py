'''
2025/12/17 daily challenge

dynamic programming approach

learnt from official editorial 2:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/editorial/#approach-2-dynamic-programming
'''


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        # dp[i][j][state] = the profit on i-th day after j transactions
        # state =
        # 0: no ongoing transaction
        # 1: during a normal transaction
        # 2: during a short selling transaction
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]

        it = enumerate(prices)
        _, v = next(it)
        # base case for day 0
        for j in range(1, k + 1):
            # no transaction, no profit
            # dp[0][j][0] = 0
            #
            # buy a stock on day 0
            dp[0][j][1] = -v
            # sell a stock short on day 0
            dp[0][j][2] = v

        # day 1~
        for i, v in it:
            for j in range(1, k + 1):
                # no ongoing transaction today, 3 situations:
                # (1) no buy or sell today
                # (2) sell a stock bought from a previous normal transaction
                # (3) short cover (buy a stock sold short previously)
                dp[i][j][0] = max(dp[i - 1][j][0],
                                  dp[i - 1][j][1] + v,
                                  dp[i - 1][j][2] - v)
                # during a normal transaction
                # (1) buy a stock today, open a normal transaction
                # (2) hold (inherit from yesterday)
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - v,
                                  dp[i - 1][j][1])
                # during a short selling
                # (1) sell a stock short
                # (2) hold (inherit from yesterday)
                dp[i][j][2] = max(dp[i - 1][j - 1][0] + v,
                                  dp[i - 1][j][2])
        return dp[-1][-1][0]

