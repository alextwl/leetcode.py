'''
dynamic programming approach

learnt from official solution 2

the idea is similar to prefix sum,
but it calculates the so-called minimum prefix width of 1's square on all cells.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        '''
        keep additional 0-index row & colmnn with zeroes.
        this helps later min() evaluation with dp[0][*] & dp[*][0] is always 0
        and we don't need to write more boundary checks for it.
        '''
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        max_width = 0  # the width of maximum 1's square
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    '''
                    get the minimum prefix width from the upper, left, and upper-left cells
                    and then plus 1 because current cell has a '1' value.
                    '''
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_width = max(max_width, dp[i][j])
        
        '''
        the problem requests for returning its area,
        so we return the sum of the largest square == width*width.
        '''
        return max_width**2

