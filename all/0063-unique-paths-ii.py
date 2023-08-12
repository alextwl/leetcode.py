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


'''
2023/08/12 daily challenge

bottom-up dynamic programming approach
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # special case: if the starting & ending cell is an obstacle
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        
        # the starting cell
        dp[0][0] = 1

        '''
        the sequence of iteration is important and
        it follows the robot which can only move either down or right.
        '''
        for x, row in enumerate(obstacleGrid):
            for y, cell in enumerate(obstacleGrid[x]):
                if cell:
                    # obstacle found
                    continue

                # get previous left cell
                left = dp[x][y-1] if y >= 1 else 0
                # get previous upper cell
                up = dp[x-1][y] if x >= 1 else 0

                # accumulate the count of pathes except the starting cell
                if x or y:
                    dp[x][y] = left + up

        return dp[-1][-1]


'''
bottom-up dynamic programming with space=O(n)
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # special case: if the starting & ending cell is an obstacle
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        prev_dp = [0] * n
        curr_dp = [0] * n
        
        # run the first row
        row_it = iter(obstacleGrid)
        col_it = iter(next(row_it))
        next(col_it)  # bypass the starting cell
        prev_dp[0] = 1
        for y, cell in enumerate(col_it, start=1):
            if cell:
                # no need to traverse to right cells because here's an obstacle
                # and no more path goes right.
                break
            prev_dp[y] = 1

        '''
        the sequence of iteration is important and
        it follows the robot which can only move either down or right.
        '''
        for row in row_it:
            for y, cell in enumerate(row):
                if cell:
                    # obstacle found, zero the cell's path count
                    curr_dp[y] = 0
                    continue

                # get previous left cell
                left = curr_dp[y-1] if y >= 1 else 0
                # get previous upper cell
                up = prev_dp[y]

                # accumulate the count of pathes except the starting cell
                curr_dp[y] = left + up
            
            '''
            let curr_dp be the next round of prev_dp,
            and recycle the prev_dp's space as a new curr_dp.
            '''
            prev_dp, curr_dp = curr_dp, prev_dp

        return prev_dp[-1]

