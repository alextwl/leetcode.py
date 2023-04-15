'''
2023/04/15 daily challenge

dynamic programming approach

try to divide the problem into subproblems.
pick lesser coins from lesser piles, and iterate the result by adding a pile/a coin each loop.

learnt from
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/solutions/3418129/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/
'''


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        '''
        dp[i][j] indicates the max value of j coins from the first i piles.
        '''
        dp = [[-1] * (k+1) for _ in range(n+1)]
        # the max values of any coins from *zero* pile are zero.
        for j in range(k+1):
            dp[0][j] = 0
        # the max values of *no* coin from any piles are also zero.
        for i in range(n+1):
            dp[i][0] = 0
        
        # iterate from the first pile to the last pile.
        for i in range(1, n+1):
            # try to maximize the money value while adding each coin
            for j in range(1, k+1):
                max_total = 0
                current_pile = piles[i-1]
                # try to pick the most j coins from the piles[i-1]
                # if piles[i] has insufficient coins, then pick at most len(piles[i]) coins.
                for coin_idx in range(min(j, len(current_pile))):
                    # note the coin_idx starts from 0, pick the first coin from the top of the pile.
                    max_total += current_pile[coin_idx]
                    '''
                    compare the maximum between the last updated dp[i][j] and
                    ((coin_idx+1) coins picked from the current pile + max value of (j - (coin_idx+1)) the first i-1 piles.
                    '''
                    dp[i][j] = max(dp[i][j],
                                   max_total + dp[i-1][j - coin_idx - 1])
                # compare dp[i][j] with
                #         no coin picked from the current_pile's result == the max value of the first i-1 piles
                # and choose the greater one.
                dp[i][j] = max(dp[i][j], dp[i-1][j])
        
        # dp[n][k] is the final ans == maximum value of k coins from all piles.
        return dp[-1][-1]

