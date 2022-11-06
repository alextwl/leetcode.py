class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        idea: buy every valley and sell every peak
        '''
        i = 0
        lastday = len(prices) - 1
        valley = peak = prices[0]
        profits = 0
        
        while(i < lastday):
            # find valley
            while(i < lastday and prices[i] >= prices[i+1]):
                i += 1
            valley = prices[i]
            # find peak
            while(i < lastday and prices[i] <= prices[i+1]):
                i += 1
            peak = prices[i]
            # obtain profit
            profits += peak - valley
        
        return profits
