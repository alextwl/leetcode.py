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

