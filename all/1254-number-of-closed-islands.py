'''
2023/04/06 daily challenge

depth first search approach
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not(0 <= i < m and 0 <= j < n):
                return 0
            
            if grid[i][j] == 1:
                return 1
            
            # grid[i][j] == 0
            grid[i][j] = 1  # visit it
            return dfs(i+1, j) & dfs(i-1, j) & dfs(i, j-1) & dfs(i, j+1)
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    islands += dfs(i, j)
        
        return islands

