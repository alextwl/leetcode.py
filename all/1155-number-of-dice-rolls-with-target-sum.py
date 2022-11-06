'''
2022/10/02 daily challenge

learnt from
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained

dynamic programming approach
reduce the problem to sub-problem with lesser dice(s) and target sum recursively
'''

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = dict()  # key=(n, target) for sub-problem
        
        def roll(d: int, target: int) -> int:
            '''
            base value: when there's no remaining dices and target sum is zeroed,
            it means last roll (d=1) is valid and has 1 possible way for target sum.
            if it's invalid, return 0 way.
            '''
            if d == 0:
                return 0 if target > 0 else 1
            
            '''
            terminate it early if it's already impossible to find a way with remaining dices.
            '''
            if d and target < 1:
                return 0
            
            # reuse existed sub-answer
            if (d, target) in dp:
                return dp[(d, target)]
            
            '''
            the number of possible ways to roll (d, k, target) is to be accumulated with dp
            '''
            ways = 0
            
            '''
            reduce the problem to d=d-1, target=target-(1..k)
            e.g. d=5, k=6, target=23
            ways = roll(d=4, target=22) + 
                   roll(d=4, target=21) +
                   roll(d=4, target=20) +
                   roll(d=4, target=19) +
                   roll(d=4, target=18) +
                   roll(d=4, target=17)
            
            the subsum must be >= 0 for a valid way to get target sum.
            '''
            for subsum in range(max(0, target - k), target):
                ways += roll(d-1, subsum)
            
            dp[(d, target)] = ways
            
            return ways
        
        return roll(n, target) % (10**9 + 7)
