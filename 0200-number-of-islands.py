'''
idea: do depth first search which visits 4 directions(NEWS) of lands
      and stops from water and grid boundary.
      count each root of tree (island) and get the number of islands.
'''

class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or \
            i >= len(grid) or j >= len(grid[0]) or \
            grid[i][j] != '1':
            # arrived water or visited land, stop searching.
            return
        
        # visit (i,j) land
        grid[i][j] = '*'
        
        # search surrounded 4 directions.
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        
        return
        
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # pick a land as a root and start DFS.
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands += 1
        
        return islands
