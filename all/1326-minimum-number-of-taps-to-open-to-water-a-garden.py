'''
2023/08/31 daily challenge

dynamic programming approach
'''

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''
        top-down dp space
        dp[i] = the minimum number of taps needed for interval [0, i]
        '''
        dp = [float('inf')] * (n+1)
        
        '''
        base case
        no taps needed for a zero interval [0, 0] which covers no garden.
        '''
        dp[0] = 0
        
        '''
        evaluate all taps from left to right
        '''
        for i, radius in enumerate(ranges):
            left = max(0, i - radius)
            right = min(i + radius, n)
            
            # update [left, right] interval
            min_taps = dp[right]
            for j in range(left, right + 1):
                '''
                2 cases:
                (1) we have the minimum taps opened.
                (2) we can have more lesser taps opened by opening j-th tap before i-th tap.
                '''
                min_taps = min(min_taps, dp[j] + 1)
            dp[right] = min_taps

        return dp[-1] if dp[-1] < float('inf') else -1

