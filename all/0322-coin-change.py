'''
bottom-up dynamic programming approach

learnt from official solution 3

count coins from $0 and find the minimum number of coins while adding money.

for example: coins = [1,2,5], amount = 11

       coin iter order ->
+---------+----+----+----+-----+
| dp\deno | $1 | $2 | $5 | min |
+---------+----+----+----+-----+
|  [$0]   | --   --   -- |  0  |
|  [$1]   |  1   --   -- |  1  |
|  [$2]   |  2    1   -- |  1  |
|  [$3]   |  3    2   -- |  2  |
|  [$4]   |  4    2   -- |  2  |
|  [$5]   |  5    3    1 |  1  |
|  [$6]   |  6    3    2 |  2  |
|  [$7]   |  7    4    2 |  2  |
|  [$8]   |  8    4    3 |  3  |
|  [$9]   |  9    5    3 |  3  |
|  [$10]  | 10    5    2 |  2  |
|  [$11]  | 11    6    3 |  3  | <- the answer
+---------+--------------+-----+
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[total amount of money] = the fewest number of coins
        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # no money, no coin.
        
        for coin in coins:
            for money in range(coin, amount + 1):
                '''
                always start from dp[the amount of money - the denomination of coin] + a coin = dp[$0] + 1
                and then dp[money+1] = min(dp[money+1], dp[$1] + 1),
                dp[money+2] = min(dp[money+2], dp[$2] + 1), ...
                and vice versa.
                '''
                dp[money] = min(dp[money], dp[money - coin] + 1)
        
        '''
        if the number of coins was infinite,
        it means we cannot make up the exact amount of money by these coins.
        '''
        return dp[-1] if dp[-1] < float('inf') else -1

