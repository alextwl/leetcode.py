'''
2025/01/28 daily challenge

depth first search approach

island variant problem
'''


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            
            fish = grid[x][y]
            grid[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                fish += dfs(dx, dy)
            return fish
        
        for r in range(m):
            for c in range(n):
                max_fish = max(max_fish, dfs(r, c))
        
        return max_fish

