'''
2023/05/25 daily challenge
2025/08/17 daily challenge

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
            '''
            e.g. maxPts=10 for i <= maxPts with the first draw,
            they have equal probability to be reached from dp[0]=1,
            so the probabilities of each destination point are:
            dp[1] = dp[0] / maxPts,
            dp[2] = dp[0] / maxPts,
            ...
            dp[10] = dp[0] / maxPts.
            (this is why the variable `window` is initialized with 1.0.)

            e.g. i=11 for the 2nd and further draws,
            there are various previous steps (11 > i >= 11-maxPts)
            which can reach i=11 with current draw, including
            from i=1 + 10 points, i=2 + 9 points, ..., i=10 + 1 point.
            so the probability of i=11 will be the sum of previous steps' probabilities.
            dp[11] = dp[1] / maxPts + \
                     dp[2] / maxPts + \
                     ...
                     dp[10] / maxPts = sum(dp[1:11]) / maxPts = window / maxPts
            '''
            dp[i] = window / maxPts

            if i < k:
                # k not yet satisfied, next draw expected.
                window += dp[i]
            else:
                # win the game because i <= n and i > k
                # we only count the winner part of probability
                ans += dp[i]

            if i - maxPts >= 0:
                # move the sliding window
                window -= dp[i-maxPts]

        return ans


'''
yet another dynamic programming + sliding window approach

learnt from official solution:
https://leetcode.com/problems/new-21-game/editorial/#solution
'''


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1

        # the sum of probability between dp[i-maxPts:k]
        curr_sum = 1 if k > 0 else 0

        for i in range(1, n + 1):
            dp[i] = curr_sum / maxPts
            if i < k:
                # insufficient points, continue drawing numbers
                curr_sum += dp[i]
            if 0 <= (diff := i - maxPts) < k:
                curr_sum -= dp[diff]

        return sum(dp[k:])

