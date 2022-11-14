'''
dynamic programming approach (time limit exceeded)

try to minimize the number of perfect squares that sum to n.
if n itself was already a perfect square, then the least number is 1.
'''

class Solution:
    def numSquares(self, n: int) -> int:
        '''
        dp[n] = the least number of perfect squares.
        
        in general we can use multiple '1' to sum to n, so the maximum ans is n for any n.
        for the convenience of min() calculation, we initialize dp elements to infinite number.
        '''
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            # try to subtract all possible perfect squares from i.
            while((jj:=j**2) <= i):
                '''
                memorize and if there's part of number had smaller amount of perfect squares, then inherit it plus 1.
                '''
                dp[i] = min(dp[i], dp[i - jj] + 1)
                j += 1
        
        return dp[-1]

