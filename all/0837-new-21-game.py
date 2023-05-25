'''
2023/05/25 daily challenge

dynamic programming + sliding window approach
'''

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= (k + maxPts):
            '''
            when k = 0, the final point is always zero and always <= n because 0 <= n.

            if points drawed could eventually fill the k and
            with the possible extra part (points gained with the last draw - k)
            it was always lesser or equal to n (that is (k + maxPts) <= n,)
            we can always win the game.
            '''
            return 1.0

        dp = [0.0] * (n+1)  # dp[i] = the probability of i points earned
        dp[0] = 1.0  # the starting point zero has probability 1.

        window = 1.0  # the sum of probabilities from the previous draws. (the point range of [i:i+maxPts])
        ans = 0.0  # the probability to win the game.

        # start from point 1.
        for i in range(1, n+1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            else:
                # win the game because i <= n and i > k
                ans += dp[i]

            if i - maxPts >= 0:
                # move the sliding window
                window -= dp[i-maxPts]

        return ans

