'''
dynamic programming approach

similar to problem 931.

start from the second row, add min(adjacent cells of upper row) to current cell,
finally the minimum value of last row is the minimum path sum.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        for i in range(1, n):
            for j in range(0, i+1):  # derive the width of current row from the height i.
                # be careful of the boundary check, the width of upper row is always shorter than current row
                triangle[i][j] += min(triangle[i-1][k] for k in range(j-1, j+1) if 0 <= k < i)        
        return min(triangle[-1])


'''
bottom-up space=O(n) approach

accumulate the minimum path sum from the bottom row,
finally the first cell will be the minimum path sum.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        dp = triangle[-1]  # use last row's space to accumulate the minimum path sum.
        
        for i in range(n-2, -1, -1):  # start from the last 2nd row.
            for j in range(0, i+1):
                '''
                if we were here:
                   2
                  3 4
                 6 5 7  <-- current row (i=2)
                4 1 8 3  <-- copied to dp row
                
                when dp = [4, 1, 8, 3]
                
                a new dp[0] = min(dp[0], dp[1]) + triangle[2][0]
                            = min(4, 1) + 6
                            = 7
                in the end of current i loop,
                the dp row will be [7, 6, 10, ... (discarded)]
                (note: dp[j] if j > i are no longer needed.)
                '''
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]
