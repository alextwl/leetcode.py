'''
2023/03/28 daily challenge

dynamic programming approach
'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366  # 0 day + 365 days
        prev_day = 0
        for i in days:
            # fill previous non-travel days:
            # assign dp[prev_day] value to dp[prev_day+1:day]
            for j in range(prev_day+1, i):
                dp[j] = dp[prev_day]

            # buy a new pass with minimum cost:
            # (1) buy 1-day pass today
            # (2) buy 7-day pass which covers i-7+1 to i day
            # (3) buy 30-day pass which covers i-30+1 to i day
            dp[i] = min(dp[i-1] + costs[0],
                        dp[max(0, i-7)] + costs[1],
                        dp[max(0, i-30)] + costs[2])

            prev_day = i

        return dp[i]

