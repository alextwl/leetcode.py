'''
2022/09/10 daily challenge
learnt from
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2555676/Python-Simple-DP-O(nk)-Uses-the-idea-of-%22reinvesting%22

DP approach

use the idea of reinvesting when k>=2,
min price may be subtracted by previous profit to get lower price.

after each round (k) of transactions were evaluated,
the last k's max profit is the final max profit.

time=O(n*k), space=O(k)
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        min_price = [1001] * (k+1)  # default to max price beyond constraints
        max_profit = [0] * (k+1)
        
        for price in prices:
            for t in range(1, k+1):
                '''
                we may reinvesting previous profit to buy in
                or sell out if more profit earned.
                '''
                min_price[t] = min(min_price[t], price - max_profit[t-1])
                max_profit[t] = max(max_profit[t], price - min_price[t])
        
        return max_profit[k]
