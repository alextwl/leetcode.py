'''
2024/08/28 daily challenge

depth first search approach

traverse island cells in multiple conditions.
'''


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n):
                return 0
            if grid2[x][y] == 0:
                return 0

            # visit the cell in grid2. (override it to zero in order to avoid revisiting it)
            grid2[x][y] = 0

            ans = 1
            # the cell in grid2 is not in the grid1,
            # fails to form the sub island.
            if grid1[x][y] == 0:
                ans = -1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if dfs(dx, dy) == -1:
                    # failed to form the sub island
                    ans = -1
            
            return ans
        
        sub_islands = 0
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j) == 1:
                    sub_islands += 1
        
        return sub_islands

