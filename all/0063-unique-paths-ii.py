'''
dynamic programming + dfs approach

similar to problem 62 Unique Paths I

let dp function return 0 for obstacle cells because no paths can pass through it.
'''

import functools

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            # if the top-left or bottom-right corner had obstacle, no path can be found.
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        @functools.cache
        def dfs(i, j):
            '''
            traverse paths to the finish cell.
            '''
            nonlocal m, n
            if i >=m or j >= n:
                return 0
            if (i, j) == (m-1, n-1):
                # the finish cell to the finish cell is always 1.
                return 1
            if obstacleGrid[i][j]:
                # encounter obstacle cell, return no path.
                return 0
            return dfs(i+1, j) + dfs(i, j+1)  # go down + go right
        # traverse from the top-left corner
        return dfs(0, 0)

