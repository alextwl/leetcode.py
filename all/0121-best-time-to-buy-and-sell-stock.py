MAX_PRICE = 10**4

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = MAX_PRICE + 1  # initial biggest val
        max_profit = 0
        
        for day in range(len(prices)):
            if prices[day] < cheapest:
                cheapest = prices[day]
            elif prices[day] - cheapest > max_profit:
                # use 'else if' to make sure
                # day of sale is after day of purchase.
                max_profit = prices[day] - cheapest
            
        return max_profit
