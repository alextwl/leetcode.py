'''
bottom-up dynamic programming approach

similar to problem 322.

accumulate the number of combinations from $0
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        dp[total amount of money] = the number of combinations
        '''
        dp = [0] * (amount + 1)
        '''
        initial case: when we use the first coin of different denominations
        it always forms the first combination.
        
        dp[100] == 0
        dp[100] += dp[0] --> dp[100] = dp[100] + dp[0] = 0 + 1 = 1
        '''
        dp[0] = 1

        for coin in coins:
            for money in range(coin, amount + 1):
                dp[money] += dp[money - coin]
        
        return dp[-1]


'''
2023/08/11 daily challenge

top-down recursive ver
'''

import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @functools.cache
        def getWays(i, amount):
            '''
            :param i: use or not to use coins[i] to make up the amount.
            :param amount: try to make the amount up.
            '''
            if amount == 0:
                return 1
            if i == len(coins):
                # there's no coins[i] so we cannot make up any amount for it.
                return 0
            
            if coins[i] > amount:
                # we cannot use coins[i] because there's insufficient amount for making up with the coin.
                return getWays(i+1, amount)
            
            '''
            ans = (1) + (2)
            (1) use the same coin for the next round of calculation with smaller amount.
            (2) not to use the current coin.
            '''
            return getWays(i, amount - coins[i]) + getWays(i+1, amount)

        # try to make up the amount from the 1st coin.
        return getWays(0, amount)

