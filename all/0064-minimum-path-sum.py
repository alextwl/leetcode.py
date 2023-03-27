'''
2023/03/27 daily challenge

dynamic programming + dfs + prefix sum approach
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        '''
        search & calculate prefix sums for each cell in the first column & first row
        since the direction of move is restricted either down or right,
        these cells' prefix sums are guaranteed minimum path sum from grid[0][0].

        initial prefix sum of example 1:
            --> --> -->
          | +---+---+---+
          v | 1 | 4 | 5 |
          | +---+---+---+
          v | 2 |   |   |
          | +---+---+---+
          v | 6 |   |   |
            +---+---+---+
        '''
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # calculate minimum prefix sum from (1,1) to (m-1, n-1).
        for i in range(1, m):
            for j in range(1, n):
                # add minimum prefix sum from upper or left cell.
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # the bottom-right corner cell has minimum path sum.
        return grid[-1][-1]

