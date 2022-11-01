'''
state machine + dynamic programming approach

draw a state machine first:

s0: noShares
s1: ownShares
s2: cooldown

start from s0
s0 --rest--> s0
s0 --buy---> s1
s1 --hold--> s1
s1 --sell--> s2
s2 --rest--> s0

the idea is try to maximize the profit by dp
with evaluating each state's profits in every round of price loop.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        initial profits for all states
        '''
        noShares = 0
        ownShares = float('-inf')  # the profit is always negative when bought the first stock
        cooldown = float('-inf')  # the profit may be negative when the investment failed
        
        for money in prices:
            '''
            evaulate all state transitions.
            
            s0 = max(rest from s0 or s2.)
            s1 = max(hold from s1 or buy from s0.)
            s2 = sold from s1
            '''
            noShares, ownShares, cooldown = max(noShares, cooldown), \
                                            max(ownShares, noShares - money), \
                                            ownShares + money
        
        # the max profit is achieved only when stock sold out.
        return max(noShares, cooldown)
