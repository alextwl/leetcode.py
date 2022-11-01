'''
state machine + dynamic programming approach

draw a state machine first:

s0: noShares
s1: ownShares

start from s0
s0 --rest--> s0
s0 --buy---> s1 (with fee incurred)
s1 --hold--> s1
s1 --sell--> s0

evaulate all state transitions just like problem 309.
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        noShares = 0
        ownShares = float('-inf')
        
        for money in prices:
            '''
            note according to example 1 the fee happens only after selling stock.
            
            s0 = max(rest from s0 or sold from s1)
            s1 = max(hold from s1 or buy from s0)
            '''
            noShares, ownShares = max(noShares, ownShares + money - fee), \
                                  max(ownShares, noShares - money)
        # the max profit is achieved only when stock sold out.
        return noShares
