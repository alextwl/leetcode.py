'''
2023/07/29 daily challenge

dynamic programming approach

learnt from official solution
https://leetcode.com/problems/soup-servings/solution/

hard level probability problem
'''

import math


class Solution:
    def soupServings(self, n: int) -> float:
        '''
        each 25 ml of soup is one serving.
        
        dp[i][j] = probability of remaining i-serving of soup A & j-serving of soup B.
        '''
        dp = {}
        dp[0] = {0: 0.5}  # dp[0][0] = half the probability that A and B become empty at the same time.
        
        '''
        there are m servings including full (25ml) & partial (<25ml) servings.
        '''
        m = math.ceil(n / 25)
        
        def serve(i, j):
            '''
            calculate probability from four kind of previous operations.
            
            the input of i & j may be >= 1 so use max() to avoid out-of-range.
            '''
            return (dp[max(0, i-4)][j] + \
                    dp[max(0, i-3)][j-1] + \
                    dp[max(0, i-2)][max(0, j-2)] + \
                    dp[i-1][max(0, j-3)]) / 4
        
        # calculate each round of serving.
        for k in range(1, m+1):
            dp[0][k] = 1  # the probability that soup A is empty first is 1
            dp[k] = {0: 0}  # soup B is empty first
            for j in range(1, k+1):
                dp[j][k] = serve(j, k)
                dp[k][j] = serve(k, j)
            # also see the proof in official solution.
            if dp[k][k] > 1 - 1e-5:
                return 1

        # start from full soups
        return dp[m][m]

