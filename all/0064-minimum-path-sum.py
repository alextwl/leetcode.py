'''
dynamic programming + dfs + prefix sum approach
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # add prefix sum of first column & first row
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # calculate minimum prefix sum from (1,1) to (m-1, n-1).
        for i in range(1, m):
            for j in range(1, n):
                # add minimum prefix sum from upper or left cell.
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        # the bottom-right corner cell has minimum path sum.
        return dp[-1][-1]

